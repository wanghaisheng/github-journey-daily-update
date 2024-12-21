---
author: Bob Johnson
cover:
  alt: cover
  square: {'error': 'exception', 'message': "Invalid URL 'image_api_url': No scheme supplied. Perhaps you meant https://image_api_url?"}
  url: {'error': 'exception', 'message': "Invalid URL 'image_api_url': No scheme supplied. Perhaps you meant https://image_api_url?"}
description: 'Yolo11 and TensorFlow.js to find and recognize objects in image, video, and webcam content.'
featured: true
keywords: {"id":"0193e86d2dbe17f260a81ba4eaa8caec","object":"chat.completion","created":1734771289,"model":"Qwen/Qwen2.5-7B-Instruct","choices":[{"index":0,"message":{"role":"assistant","content":"### Keywords\n- YoloDetect\n- Yolo11\n- TensorFlow.js\n- Object Detection\n- Image Recognition\n- Video Recognition\n- Webcam\n- React\n- Machine Learning\n- Ultralytics\n- YOLO11 Nano Object Detection Model\n- Vite\n- Git\n- Web Application\n- Bounding Boxes\n- Confidence Scores\n- HTML\n- CSS\n- JavaScript\n- Vercel\n- Deployment\n\n### Tags\n#YoloDetect #YOLO11 #TensorFlowJS #ObjectDetection #ImageRecognition #VideoRecognition #Webcam #React #MachineLearning #Ultralytics #YOLO #HTML #CSS #JavaScript #Vite #Git #WebApplication #BoundingBoxes #ConfidenceScores #Vercel #Deployment"},"finish_reason":"stop"}],"usage":{"prompt_tokens":972,"completion_tokens":159,"total_tokens":1131},"system_fingerprint":""}
layout: ../../layouts/MarkdownPost.astro
meta:
- content: Bob Johnson
  name: author
- content: {"id":"0193e86d2dbe17f260a81ba4eaa8caec","object":"chat.completion","created":1734771289,"model":"Qwen/Qwen2.5-7B-Instruct","choices":[{"index":0,"message":{"role":"assistant","content":"### Keywords\n- YoloDetect\n- Yolo11\n- TensorFlow.js\n- Object Detection\n- Image Recognition\n- Video Recognition\n- Webcam\n- React\n- Machine Learning\n- Ultralytics\n- YOLO11 Nano Object Detection Model\n- Vite\n- Git\n- Web Application\n- Bounding Boxes\n- Confidence Scores\n- HTML\n- CSS\n- JavaScript\n- Vercel\n- Deployment\n\n### Tags\n#YoloDetect #YOLO11 #TensorFlowJS #ObjectDetection #ImageRecognition #VideoRecognition #Webcam #React #MachineLearning #Ultralytics #YOLO #HTML #CSS #JavaScript #Vite #Git #WebApplication #BoundingBoxes #ConfidenceScores #Vercel #Deployment"},"finish_reason":"stop"}],"usage":{"prompt_tokens":972,"completion_tokens":159,"total_tokens":1131},"system_fingerprint":""}
  name: keywords
pubDate: '2024-12-21 15:27:08'
tags:
- {"id":"0193e86d2dbe17f260a81ba4eaa8caec","object":"chat.completion","created":1734771289,"model":"Qwen/Qwen2.5-7B-Instruct","choices":[{"index":0,"message":{"role":"assistant","content":"### Keywords\n- YoloDetect\n- Yolo11\n- TensorFlow.js\n- Object Detection\n- Image Recognition\n- Video Recognition\n- Webcam\n- React\n- Machine Learning\n- Ultralytics\n- YOLO11 Nano Object Detection Model\n- Vite\n- Git\n- Web Application\n- Bounding Boxes\n- Confidence Scores\n- HTML\n- CSS\n- JavaScript\n- Vercel\n- Deployment\n\n### Tags\n#YoloDetect #YOLO11 #TensorFlowJS #ObjectDetection #ImageRecognition #VideoRecognition #Webcam #React #MachineLearning #Ultralytics #YOLO #HTML #CSS #JavaScript #Vite #Git #WebApplication #BoundingBoxes #ConfidenceScores #Vercel #Deployment"},"finish_reason":"stop"}],"usage":{"prompt_tokens":972,"completion_tokens":159,"total_tokens":1131},"system_fingerprint":""}
theme: light
title: YoloDetect
---

# YoloDetect

## Repository URL: 
[https://github.com/wanghaisheng/YoloDetect](https://github.com/wanghaisheng/YoloDetect)

## Stars: 
**0**

## Forks: 
**0**

## Description: 
Yolo11 and TensorFlow.js to find and recognize objects in image, video, and webcam content.

## README Content: 
# YoloDetect

This is a simple web app to demonstrate how to use Yolo11 and TensorFlow.js to identify and locate objects within images, videos, and live camera feeds.

## Project Structure

The project is structured as follows:

- `assets/`: This directory contains screenshots of the output results and deployment-related reports.

- `public/`: Static assets like images, icons, and fonts. Also contains the Yolo11 model folder.

  - `yolo11n_web_model/`: Contains the Yolo11 nano object detection model files for tensorflow.js format.

- `src/`: Core source code for the application.

  - `components/`: Reusable React components for the application.

    - `btn-handler.jsx`: Button handler component for managing button actions.
    - `loader.jsx`: Loader component for displaying loading state.

  - `style/`: CSS files for styling the application.

    - `index.css`: Global CSS styles for the application.
    - `loader.css`: CSS styles for the loader component.
    - `App.css`: CSS styles for the main application.

  - `utils/`: Utility functions for the application.

    - `detect.js`: Object detection utility js function.
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
- **Ultralytics**: Exported YOLO11 nano detection model to TensorFlow.js.

## Getting Started

To get started with this project, follow the steps below:

1. Clone the repository: `git clone https://github.com/sitamgithub-MSIT/YoloDetect.git`
2. Change the directory: `cd YoloDetect`
3. Install the required dependencies: `npm install`
4. Run the application: `npm run dev`

Open your local host to view the web application in your browser at `http://localhost:5173/`. You can also access a live version of the application [here](https://yolo-detect.vercel.app/), which is deployed on Vercel.

## Results

The YoloDetect web application allows users to upload an image or video file, or use their webcam to detect and locate objects within the media. The application uses the Yolo11 object detection model to identify objects in the media and draw bounding boxes around them. The detected objects are displayed with their corresponding confidence scores.

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

