def flipText(text_input_file, text_output_file):

	for line in open(text_input_file).readlines():
		stripped_line = line.strip()
		words = stripped_line.split('\t')
		final_list = '\t'.join(words[::-1])
		with open(text_output_file, "a") as f:
			f.write(final_list + "\n")

if __name__ == "__main__":
	flipText('input.txt', 'output.txt')
