---
author: Jane Smith
cover:
  alt: cover
  square: https://fluxapi.borninsea.com/image/image_1734782702518_e0xdmn
  url: https://fluxapi.borninsea.com/image/image_1734782702518_e0xdmn
description: 'Yolo11 and TensorFlow.js to find and recognize objects in image, video, and webcam content.'
featured: true
keywords: 

- YoloDetect
- Yolo11
- TensorFlow.js
- object detection
- image
- video
- webcam
- web app
- React
- machine learning
- model
- Git
- Vite
- HTML
- CSS
- JavaScript
- Ultralytics
- Vercel

These keywords cover the main topics and technologies discussed in the project description.
layout: ../../layouts/MarkdownPost.astro
meta:
- content: Jane Smith
  name: author
- content: 

- YoloDetect
- Yolo11
- TensorFlow.js
- object detection
- image
- video
- webcam
- web app
- React
- machine learning
- model
- Git
- Vite
- HTML
- CSS
- JavaScript
- Ultralytics
- Vercel

These keywords cover the main topics and technologies discussed in the project description.
  name: keywords
pubDate: '2024-12-21 15:27:08'
tags:
- tensorflow.js,yolov11,yolodetect,object_detection,web_app,react,webcam,video,static_assets,deployment,gitignore,license,README,html,css,js,machine_learning,web_interface,vercel,ultralytics,vite_config
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

