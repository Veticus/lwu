from unittest import TestCase
from intmod.preflight.syntax_parse import parse_input_string


class TestSyntaxParse(TestCase):
	def test_input_length_multi_pospair(self):
		input_str = "shovel 4 v4 e5"
		expected_output = (['e', 'h', 'l', 'o', 's', 'v'], [4], ['v4', 'e5'], "", "")
		self.assertEqual(expected_output, parse_input_string(input_str))

	def test_input_nolength_multi_pospair(self):
		input_str = "shovel v4 e5"
		expected_output = (['e', 'h', 'l', 'o', 's', 'v'], [], ['v4', 'e5'], "", "")
		self.assertEqual(expected_output, parse_input_string(input_str))

	def test_input_length_single_pospair(self):
		input_str = "shovel 4 v4"
		expected_output = (['e', 'h', 'l', 'o', 's', 'v'], [4], ['v4'], "", "")
		self.assertEqual(expected_output, parse_input_string(input_str))

	def test_input_nolength_single_pospair(self):
		input_str = "shovel e5"
		expected_output = (['e', 'h', 'l', 'o', 's', 'v'], [], ['e5'], "", "")
		self.assertEqual(expected_output, parse_input_string(input_str))

	def test_input_length_no_pospair(self):
		input_str = "shovel 4"
		expected_output = (['e', 'h', 'l', 'o', 's', 'v'], [4], [], "", "")
		self.assertEqual(expected_output, parse_input_string(input_str))

	def test_input_nolength_no_pospair(self):
		input_str = "shovel"
		expected_output = (['e', 'h', 'l', 'o', 's', 'v'], [], [], "", "")
		self.assertEqual(expected_output, parse_input_string(input_str))

	def test_input_length_multi_pospair_out_of_order(self):
		input_str = "4 v4 shovel"
		expected_output = (['e', 'h', 'l', 'o', 's', 'v'], [4], ['v4'], "", "")
		self.assertEqual(expected_output, parse_input_string(input_str))

	def test_command_noarg(self):
		input_str = ":command"
		expected_output = ([], [], [], "command", "")
		self.assertEqual(expected_output, parse_input_string(input_str))

	def test_command_arg(self):
		input_str = ":command argument"
		expected_output = ([], [], [], "command", "argument")
		self.assertEqual(expected_output, parse_input_string(input_str))
