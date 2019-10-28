/*
 * Usage:
 * dtrace -s script.d -p PROCESS_PID
 * or
 * dtrace -s script.d -c BINARY
 */
fbt::vkbd_read_char:return / args[1] == 0x58/ {
	pr = 1;
}

pid$target:::entry /pr != 1/{
	tab[probefunc] = 1;
}

pid$target:::entry /pr == 1 && tab[probefunc] != 1/ {
	tab[probefunc] = 1;
	printf("%s", probefunc);
}

