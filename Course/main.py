from flask import Flask, render_template, request
import markdown
import os, re

app = Flask(__name__)
app.config['SECRET_KEY'] = 'fjewnsakewjiufewh74'

def extract_between_strings(text, start, end):
    pattern = re.compile(re.escape(start) + '(.*?)' + re.escape(end), re.DOTALL)
    match = pattern.search(text)
    if match:
        return match.group(1)
    else:
        return None
def replace_between_strings(text, start, end, replacement):
    pattern = re.compile(re.escape(start) + '(.*?)' + re.escape(end), re.DOTALL)
    return pattern.sub(lambda match: replacement, text)
def extract_flashcards(content):
    flashcards = []
    pattern = re.compile(r'%flashcard%(.*?)%end flashcard%', re.DOTALL)
    matches = pattern.findall(content)
    for match in matches:
        flashcards.append(match.strip())
    return flashcards

@app.route('/')
def hello():
    return render_template("home.html")
@app.route('/course/<lesson_name>')
def course(lesson_name):
    markdown_file = os.path.join(app.root_path, f'templates/markdown/{lesson_name}.md')
    with open(markdown_file, 'r') as f:
        markdown_content = f.read()

    # Convert Markdown content to HTML
    html_content = markdown.markdown(markdown_content)
    i = 0
    if "<em>" in html_content:
        html_content = html_content.replace("<em>", "<em><span class='italics'>")
        html_content = html_content.replace("</em>", "</span></em>")
    while True:
        i += 1
        if f"%image{i}%" in html_content:
            image_file = extract_between_strings(html_content, f"%image{i}%", f"%end image{i}%")
            html_content = replace_between_strings(html_content, f"%image{i}%", f"%end image{i}%", f"<img src='/static/Images/{image_file}' alt=''>")
        if f"%flashcard block{i}%" in html_content:
            flashcard_block_content = extract_between_strings(html_content, f"%flashcard block{i}%", f"%end flashcard block{i}%")
            flashcard_content_list = extract_flashcards(flashcard_block_content)
            individual_flashcards = []
            for flashcard_content in flashcard_content_list:
                front = extract_between_strings(flashcard_content, "%front%", "%end front%")
                back = extract_between_strings(flashcard_content, "%back%", "%end back%")
                flashcard_html = f""" 
                <div class="flashcard">
                    <div class="front">
                        <p>{front}</p>
                    </div>
                    <div class="back">
                        <p>{back}</p>
                    </div>
                </div>
                """
                individual_flashcards.append(flashcard_html)
            flashcard_html = "".join(individual_flashcards)
            flashcard_block_html = f"""
            <div class="flashcard-div">
                {flashcard_html}
            </div>
            """
            html_content = replace_between_strings(html_content, f"%flashcard block{i}%", f"%end flashcard block{i}%", flashcard_block_html)
        if f"%multi-choice{i}%" in html_content:
            multi_choice_block_content = extract_between_strings(html_content, f"%multi-choice{i}%", f"%end multi-choice{i}%")
            question1 = extract_between_strings(multi_choice_block_content, "%question1%", "%choices%")
            choices = extract_between_strings(multi_choice_block_content, "%choices%", "%end choices%")
            choices = choices.split("\n")
            answer = extract_between_strings(multi_choice_block_content, "%answer%", "%end answer%")
            answer = answer.replace("\n", "")
            choices_html = ""
            for n in choices:
                if n != '':
                    choices_html += f"""
                        <div class="choice" id="{n}" onclick="selected(this)">
                            <span class="answer-circle"></span>
                            {n}
                        </div>
                    """
            multi_choice_html = f"""
            <div class="choice-box" answer="{answer}">
                <p style="margin-left: 2ch; margin-right: 2ch;">{question1}</p>
                {choices_html}
                <div class="row" style="padding: 1rem;">
                    <div class="retry-button" onclick="retry()">&#x21BB; Retry</div>
                    <div class="submit-button" onclick="submit()">Submit</div>
                </div>
            </div>
            """
            html_content = replace_between_strings(html_content, f"%multi-choice{i}%", f"%end multi-choice{i}%", multi_choice_html)
        if f"%gap-fill{i}%" in html_content:
            gap_fill_content = extract_between_strings(html_content, f"%gap-fill{i}%", f"%end gap-fill{i}%")
            gap_fill_content = gap_fill_content.replace("%_%", '<input type="text" class="missing-word"/>')
            gap_fill_html = f"""
                <div class="gap-fill">
                    <p>
                    Fill in the blank:
                    <br>
                    {gap_fill_content}
                    </p>
                </div>
            """
            html_content = replace_between_strings(html_content, f"%gap-fill{i}%", f"%end gap-fill{i}%", gap_fill_html)
        if f"%single-answer{i}%" in html_content:
            single_answer_content = extract_between_strings(html_content, "%question%", f"%end single-answer{i}%")
            single_answer_html = f"""
                <div class="question">
                    {single_answer_content}
                    <input type="text" class="answer"/>
                </div>
            """
            html_content = replace_between_strings(html_content, f"%single-answer{i}%", f"%end single-answer{i}%", single_answer_html)
        else:
            break
    return render_template('course.html', html_content=html_content)
@app.route('/log-message', methods=['POST'])
def log_message():
    message = request.form['message']
    return 'Message logged successfully', 200
if __name__ == '__main__':
    app.run(debug=True)