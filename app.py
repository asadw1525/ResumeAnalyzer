import gradio as gr
from analyzer import analyze_resume

with gr.Blocks(title="Resume Analyzer & Job Fit Generator", theme=gr.themes.Soft()) as demo:
    with gr.Column():
        gr.Markdown(
            """
            <h1 style='text-align: center; font-weight: bold; font-size: 30px; color: #2B5876;'>📄 Resume Analyzer & Job Fit Generator</h1>
            <p style='text-align: center; font-size: 16px;'>Upload your resume and let AI suggest personalized job roles, industries, and improvements.</p>
            """
        )

        gr.Markdown("<h2 style='font-weight: bold;'>📁 Upload Your Resume</h2>")
        file_input = gr.File(label="Upload Resume (PDF Only)", file_types=[".pdf"], type="filepath")
        analyze_button = gr.Button("🔍 Analyze Resume", variant="primary")
        gr.Markdown("<hr style='margin: 20px 0;'>")
        gr.Markdown("<h2 style='font-weight: bold;'>🎯 Suggested Job Titles and Insights</h2>")
        output_box = gr.Markdown()

        analyze_button.click(fn=analyze_resume, inputs=file_input, outputs=output_box)

demo.launch(debug=True, share=True)
