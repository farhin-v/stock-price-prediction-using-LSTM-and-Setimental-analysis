import gradio as gr

def predict(stock):
    return f"Stock prediction generated for {stock}"

demo = gr.Interface(
    fn=predict,
    inputs="text",
    outputs="text",
    title="AI Stock Price Prediction System"
)

demo.launch()
