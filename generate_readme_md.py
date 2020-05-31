with open('./README.md.template', 'r') as readme_template_file:
    readme_template = readme_template_file.read()
    with open('./test.py', 'r') as code_file:
        code_string = code_file.read()
        with open('./README.md', 'w') as readme_file:
            readme_file.write(readme_template.format(code=code_string))
