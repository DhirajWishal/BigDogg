import pydoodle
import os
import urllib3

language_dictionary = {
    ".c": "c",
    ".cpp": "cpp17",
    ".cxx": "cpp17",
    ".py": "python3",
}

language_list =[
    ".c", ".cpp", ".cxx",
    ".py"
]

compiler = pydoodle.Compiler(clientId=os.environ["PYDOODLE_CLIENT_ID"],
                             clientSecret=os.environ["PYDOODLE_CLIENT_SECRET"])


def process_language(lang):
    """
    Process the input language to whats supported by PyDoodle.
    :param lang: The input language format.
    :return: The processed language format.
    """

    if lang == "python":
        lang = "python3"

    elif lang == "c++":
        lang = "cpp17"

    elif lang == "C#":
        lang = "csharp"

    elif lang == "objectivec" or lang == "objective c":
        lang = "objc"

    elif lang == "f#":
        lang = "fsharp"

    return lang


def execute_attachments(attachments):
    """
    Execute a number of attachments.
    :param attachments: The attachment list.
    :return: The return statement.
    """
    output_details = ""
    for attachment in attachments:
        http = urllib3.PoolManager()
        file = http.request('POST', attachment.url, preload_content=False)
        script = file.data

        language = ""
        for ending in language_list:
            if ending in attachment.filename:
                language = language_dictionary[ending]

        if language == "":
            return "Looks like you, the dumb fuck made a mistake. Am I a fucking joke to you? Send me a source file not a random ass file retard..."

        result = compiler.execute(script=script.decode("utf-8"), language=language)
        output_details += f"""
```
For attachment: {attachment.filename}
Result: {result.output}
Status Code: {result.statusCode}
CPU Time: {result.cpuTime} us.
Memory Usage: {result.memory} Bytes.
Number of available uses: {200 - compiler.usage()}
```
        """
        file.release_conn()

    return output_details


def execute(content):
    """
    Execute a command. By default python single line codes are allowed.
    :param content: The content containing the code.
    :return: The executed result.
    """
    input_list = content.split("\n")

    if len(input_list) < 4:
        return "Looks like your too dumb to use this command. Go chek `dogg help` and come back when your smart enough."

    language = process_language(input_list[1].strip('`'))

    script = ""
    for line in range(2, len(input_list) - 1):
        script += input_list[line] + "\n"

    result = compiler.execute(script=script, language=language)

    return f"""
```
Result: {result.output}
Status Code: {result.statusCode}
CPU Time: {result.cpuTime} us.
Memory Usage: {result.memory} Bytes.
Number of available uses: {200 - compiler.usage()}
```
    """

# result = c.execute(script="print('Hello World')", language="python3")
# usage = c.usage()
# print(usage, result.output, sep='\n')
