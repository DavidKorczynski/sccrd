#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

extern "C" int LLVMFuzzerTestOneInput(const uint8_t *data, size_t size) {
	if (size < 5) {
		return 0;
	}
	if (data[0] + data[1] > 20) {
		return data[123];
	}
	return 0;
}
