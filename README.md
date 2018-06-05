# When Wor(l)d Collide
We are all cyborgs. We all have two lives; one physical, the other digital. 'When Wor(l)ds Collide' investigates contentions of the world of cyborg that takes issue with borders, disruptions of representation and creates noise. It has been developed as a fraught landscape, which explores material and significant opportunities for competing experimental language use that directly and interfere with the experience. What are the inherent contradictions, harmonies and conflicts that will arise from such an interaction? That is what we are bound to explore.


The facial expression detection and artificial intelligence components of the When Wor(l)ds Collide Project. The keras model is trained with FER-2013 dataset using CNN model. 

# Requirements
- openCV 3.2.0
- keras 2.0.5
- tensorflow 1.1.0
- pandas 0.19.1
- numpy 1.12.1
- h5py 2.7.0
- statistics

# Running
After installing the required libraries listed above, run the command: `python expression_classifier.py`

The code provided includes pieces to provide UDP connection to transfer facial expression data into another computer. After running the program, the facial expression data will be available in the specified IP and PORT for external use. In order to communicate with the chosen software, please modify this part of the code:

```
import socket
UDP_IP = "123.68.9.1"
UDP_PORT = 5550
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
```

# License
MIT License

Copyright (c) 2018 When Wor(l)ds Collide Team

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER IABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE. 