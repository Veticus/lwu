import sys

from icecream import ic


def determine_output_mode(args):
	"""
	Checks if the output of the program will be sent to a pipe, stdout, the fastapi or the json output.

	If the -j or --json flag is true, this will return "JSON", so the main knows to send all output via the JSON oudput module.
	If the -a or --fastapi flag is true, this will return "FASTAPI", so the main knows to not print anything.

	If the programs output is sent to stdout it will return "STDOUT", so the main knows to just use normal prints.
	(And icecream if -d is set)

	If the programs output is sent to a pipe, it will return "PIPE", so the main knows to print very simple output.

	If none of those cases match, it will return "STDOUT", assuming that the OS is making it hard to detect if the output is being piped.
	In that case it is preferred to preserve the "normal" CLI functionality.

	:param args: an arpgparse args dict.
	:return: The output mode as a string.
	"""

	if args.d:
		ic("--- BEGINNING OF determine_output_mode() ---")

	# TODO: Implement error handling, in case something goes wrong with the isatty() call
	if not sys.stdout.isatty():
		if args.d:
			ic("Recommending PIPE output mode because sys.stdout.isatty() is not truthy.")
			ic(sys.stdout.isatty())
		return "PIPE"
	else:
		if args.d:
			ic("Not recommending PIPE, but still moving on.")

	if args.json:
		if args.d:
			ic("Recommending JSON output mode, because --json or -j are used.")
		return "JSON"
	else:
		if args.d:
			ic("Not recommending JSON output mode, but still moving on.")

	if args.fast_api:
		if args.d:
			ic("Recommending FASTAPI output mode, because -a or --fastapi are used.")
		return "FASTAPI"
	else:
		if args.d:
			ic("Not recommending FASTAPI output mode, but still moving on.")

	ic("--- END OF determine_output_mode() ---")
	return "STDOUT"
