export TRACE_DUMP=`basename "${TRACE_BIN}"`.gdb
nm --format posix ${TRACE_BIN} | \
  awk '
  BEGIN {
    print "set breakpoint pending on"
  }
  {
    print "tbreak " \
      gensub(/@@.*$/, "", "g", $1)
  }' > ${TRACE_DUMP}
gdb  --quiet -x ${TRACE_DUMP} ${TRACE_BIN}
