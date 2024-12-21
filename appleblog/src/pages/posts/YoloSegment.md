---
author: Bob Johnson
cover:
  alt: cover
  square: {'error': 'exception', 'message': "Invalid URL 'image_api_url': No scheme supplied. Perhaps you meant https://image_api_url?"}
  url: {'error': 'exception', 'message': "Invalid URL 'image_api_url': No scheme supplied. Perhaps you meant https://image_api_url?"}
description: 'Yolo11 and TensorFlow.js to segment or partition images according to their content.'
featured: true
keywords: {"id":"0193e86d3b6d3960d8dd19eca8746099","object":"chat.completion","created":1734771293,"model":"Qwen/Qwen2.5-7B-Instruct","choices":[{"index":0,"message":{"role":"assistant","content":"### Keywords\n- YoloSegment\n- Yolo11\n- TensorFlow.js\n- Image segmentation\n- Web app\n- React\n- Machine learning\n- Webcam\n- Deployment\n- Ultralytics\n\n### Tags\n- #image-segmentation #YOLO #TensorFlow #web-application #ReactJS #machine-learning #webcam #deployment #Ultralytics #github #MIT-license"},"finish_reason":"stop"}],"usage":{"prompt_tokens":955,"completion_tokens":82,"total_tokens":1037},"system_fingerprint":""}
layout: ../../layouts/MarkdownPost.astro
meta:
- content: Bob Johnson
  name: author
- content: {"id":"0193e86d3b6d3960d8dd19eca8746099","object":"chat.completion","created":1734771293,"model":"Qwen/Qwen2.5-7B-Instruct","choices":[{"index":0,"message":{"role":"assistant","content":"### Keywords\n- YoloSegment\n- Yolo11\n- TensorFlow.js\n- Image segmentation\n- Web app\n- React\n- Machine learning\n- Webcam\n- Deployment\n- Ultralytics\n\n### Tags\n- #image-segmentation #YOLO #TensorFlow #web-application #ReactJS #machine-learning #webcam #deployment #Ultralytics #github #MIT-license"},"finish_reason":"stop"}],"usage":{"prompt_tokens":955,"completion_tokens":82,"total_tokens":1037},"system_fingerprint":""}
  name: keywords
pubDate: '2024-12-21 15:27:08'
tags:
- {"id":"0193e86d3b6d3960d8dd19eca8746099","object":"chat.completion","created":1734771293,"model":"Qwen/Qwen2.5-7B-Instruct","choices":[{"index":0,"message":{"role":"assistant","content":"### Keywords\n- YoloSegment\n- Yolo11\n- TensorFlow.js\n- Image segmentation\n- Web app\n- React\n- Machine learning\n- Webcam\n- Deployment\n- Ultralytics\n\n### Tags\n- #image-segmentation #YOLO #TensorFlow #web-application #ReactJS #machine-learning #webcam #deployment #Ultralytics #github #MIT-license"},"finish_reason":"stop"}],"usage":{"prompt_tokens":955,"completion_tokens":82,"total_tokens":1037},"system_fingerprint":""}
theme: light
title: YoloSegment
---

# YoloSegment

## Repository URL: 
[https://github.com/wanghaisheng/YoloSegment](https://github.com/wanghaisheng/YoloSegment)

## Stars: 
**0**

## Forks: 
**0**

## Description: 
Yolo11 and TensorFlow.js to segment or partition images according to their content.

## README Content: 
2024-12-18

# YoloSegment

This simple web app demonstrates how to use Yolo11 and TensorFlow.js to divide images into different regions or segments based on their content.

## Project Structure

The project is structured as follows:

- `assets/`: This directory contains screenshots of the output results and deployment-related reports.

- `public/`: Static assets like images, icons, and fonts. Also contains the Yolo11 model folder.

  - `yolo11n-seg_web_model/`: Contains the Yolo11 nano segmentation model files for tensorflow.js format.

- `src/`: Core source code for the application.

  - `components/`: Reusable React components for the application.

    - `btn-handler.jsx`: Button handler component for managing button actions.
    - `loader.jsx`: Loader component for displaying loading state.

  - `style/`: CSS files for styling the application.

    - `index.css`: Global CSS styles for the application.
    - `loader.css`: CSS styles for the loader component.
    - `App.css`: CSS styles for the main application.

  - `utils/`: Utility functions for the application.

    - `detect.js`: Image segmentation utility js function.
    - `renderBox.js`: Box rendering utility js function.
    - `webcam.js`: Webcam utility js function.
    - `labels.json`: Labels for the Yolo11 model classes in JSON format.

  - `App.jsx`: Main React component for the application.
  - `main.jsx`: Entry point for the application.

- `.gitignore`: Specifies which files and directories should be ignored by Git.
- `LICENSE`: Project licensing information.
- `README.md`: Project documentation and setup instructions.
- `index.html`: Main HTML file for the application.
- `package.json`: Project dependencies and script configuration.
- `vite.config.js`: Vite configuration file for the project.

## Technologies Used

- **HTML**: Standard markup language for creating web pages.
- **CSS**: Style sheet for designing the layout of web pages.
- **JavaScript**: High-level programming language for building web applications.
- **React**: JavaScript library for building user interfaces.
- **TensorFlow.js**: Machine learning library for training and deploying machine learning models in the browser and Node.js.
- **Ultralytics**: Exported YOLO11 nano segmentation model to TensorFlow.js.

## Getting Started

To get started with this project, follow the steps below:

1. Clone the repository: `git clone https://github.com/sitamgithub-MSIT/YoloSegment.git`
2. Change the directory: `cd YoloSegment`
3. Install the required dependencies: `npm install`
4. Run the application: `npm run dev`

Open your local host to view the web application in your browser at `http://localhost:5173/`. You can also access a live version of the application [here](https://yolo-segment.vercel.app/), which is deployed on Vercel.

## Results

The YoloSegment web application allows users to upload an image or use their webcam to segment the image into different regions based on the content. The application uses the Yolo11 segmentation model to achieve this functionality.

**Note**: To see results regarding testing and deployment, please refer to the `assets` folder in the repository.

## References

The following resources were used to develop this project:

- [Yolo11](https://docs.ultralytics.com/models/yolo11/)
- [TensorFlow.js](https://www.tensorflow.org/js)
- [Ultralytics](https://github.com/ultralytics/ultralytics)

Special thanks to Wahyu Setianto for his contributions to projects involving the YOLO series of models, ONNX, TensorFlow.js, and more.

## Contributing

Contributions are welcome! If you would like to contribute to this project, please raise an issue to discuss the changes you would like to make. Once the changes are approved, you can create a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contact

If you have any questions or suggestions regarding the project, feel free to reach out to me on my GitHub profile.

Happy coding! 🚀

