from intmod.preflight.arghandling import handle_args
from intmod.preflight.output_mode_detection import determine_output_mode
from intmod.modes.interactive import interactive_main

if __name__ == '__main__':
	args = handle_args()
	output_mode = determine_output_mode(args)

	if output_mode == "STDOUT":
		interactive_main()
