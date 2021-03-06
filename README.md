# Vector-CLI

![](https://raw.githubusercontent.com/kunal-mahatha/Vector-CLI/main/img/Vector-CLI.gif?token=APVZASYVYFGDNPZON4IRPTTA3YHNS)

## About the Tool
This is a CLI tool for operation on Vector Quantities.

## Features
 - Finds position vector from given two different points in a space.
 
 - Obtains Magnitude of a Vector.
 - Detects Direction of a Vector.
 - Checks whether the given two vectors are Perpendicular or not.
 - Interactive terminal Interface.

## Dependency
 - Install pyinstaller for creating executable file
```python3
pip install pyinstaller
```
 
 ### Usage
 
 ![](https://raw.githubusercontent.com/kunal-mahatha/Vector-CLI/main/img/demonstration.gif?token=APVZAS6OIHELIGUY3DVMUG3A33ADK)
 
 To use this :
  - Clone the Repository
  ```python3
  git clone https://github.com/kunal-mahatha/Vector-CLI.git
  ```
  - locate the `vector.py`
  ```python3
  cd Vector-CLI
  ```
  - make a executable file of `vector.py`
  ```python
  pyinstaller --onefile vector.py
  ```
  - locate the `vector` exe file
  ```python
  cd dist/vector
  ```
   - locate 
  ```python
  cd $HOME/.local/bin
  ```
  - copy the `vector` exe file to the path variable
  ```python
  cp Vector-CLI/dist/vector
  ```
  - run the `vector` file
  ```python
  vector
  ```


[![MasterHead](https://github.com/kunal-mahatha/Vector-CLI/blob/main/img/4.jpg)](https://username.github.io)

  - Hit Enter to continue
  ```python
                
  ```



  ## Exploring the Menu Options
  
  [![MasterHead](https://github.com/kunal-mahatha/Vector-CLI/blob/main/img/5.jpg)](https://username.github.io)
  
  #
  
  Options | Feature | Explaination
  :---:|:--- |:---
  1 | Find the Position Vector | Takes two points in space and finds the position vector
  2 | Find the Magnitude of the Vector | Takes the position vector and finds its magnitude
  3 | Find if the vectors are perpendicular     | Takes two vectors and checks whether they are perpendicular or not
  4 | Find the Direction of the vector | Takes the vector and finds the unit vector
  5 | Exit | 
  #
  
   ### 1. Find the Position Vector
   - Type "1"
   ```python
   Enter your Choice : 1
   ```
   - Enter the position of first point separated by comma
   ```python
   Enter the position 1 : 1,2,3
   ```
   - Enter the position of first point separated by comma
   ```python
   Enter the position 2 : 2,1,2
   ```
   - Output 
   ```python
   The position vector is along -1i + 1j + 1k
   ```
   ### 2. Find the Magnitude of the Vector
   - Type "2"
   ```python
   Enter your Choice : 2
   ```
   - Enter the arguements of position vector separated by comma
   ```python
   Enter the arguements of position vector separated by comma : 1,2,3
   ```
   - Output
   ```python
   The Magnitude of the Vector is  3.74
   ```
   ### 3. Find if the vectors are perpendicular
   - Type "3"
   ```python
   Enter your Choice : 3
   ```
   - Enter the position of first point separated by comma
   ```python
   Enter the position 1 : 1,2,3
   ```
   - Enter the position of first point separated by comma
   ```python
   Enter the position 2 : 3,4,1
   ```
   - Output 
   ```python
   Nope ! The Vectors are not Perpendicular
   ```
   ### 4. Find the Direction of the vector
   - Type "4"
   ```python
   Enter your Choice : 4
   ```
   - Enter the arguements of position vector separated by comma
   ```python
   Enter the position separated by comma : 1,2,3
   ```
   - Output
   ```python
   The Direction of the vector is along 0.07i + 0.14j + 0.21k
   ```
   ### 5. Exit
   - Type "5"
   ```python
   Enter your Choice : 5
   ```
 ---
   
   ## Demo Video
   To view the Video [Click Here](https://www.youtube.com/watch?v=LSCWQ66JaXA)

   
 ---
 ## COMING SOON !!
 I aim to make a data structure for visual vector operations from scratch like sympy, numpy, etc. for python.
 
 - One can do every vector operation
 
 - One can visualise those in graphical manner
 
 ---
   
   ## JFK ( Just for Knowledge )
   
   ### What is a scalar ?
   **A Scalar** or **Scalar Quantity** is a quantity that can be described by a single element of a number field, such as a real number, often accompanied by units of measurement
   
   ### What is a vector ?
   **A Vector** or **Vector Quantity** is a quantity that has both magnitude and direction. It is typically represented by an arrow whose direction is the same as that of the quantity and whose length is proportional to the quantity's magnitude. Although a vector has magnitude and direction, it does not have position.
