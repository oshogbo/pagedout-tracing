# Usage: python script.py BINARY PROCESS_PID

from bcc import BPF
from ctypes import *
import time, sys, signal

def printe(cpu, data, size):
    global sp
    if not sp:
        return
    # Read addr and convert it to symbol!
    addr = cast(
        data, POINTER(c_uint64)
    ).contents.value
    print(
        "{} {}".format(hex(addr), b.sym(addr, pid))
    )

def chsp(sig, frame):
    global sp
    if sp:
        exit()
    print("Starting loging.")
    sp = True

sp = False
pid = int(sys.argv[2])
signal.signal(signal.SIGINT, chsp)
b = BPF(text="""
#include <uapi/linux/ptrace.h>

BPF_HASH(funcs, uint64_t, int);
BPF_PERF_OUTPUT(events);

int trace_func(struct pt_regs *ctx) {
    uint64_t addr = PT_REGS_IP(ctx);
    int val = 1;

    /* Notify python that we visited new function. */
    if (funcs.lookup(&addr) == NULL) {
        events.perf_submit(ctx,
            &addr, sizeof(addr));
    }
    funcs.insert(&addr, &val);
    return 0;
}
""")
b.attach_uprobe(name=sys.argv[1], sym_re='.*',
        fn_name="trace_func", pid=pid)
b['events'].open_perf_buffer(printe)

print "READY"
while True:
    b.perf_buffer_poll()
