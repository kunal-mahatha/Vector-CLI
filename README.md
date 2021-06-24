# Vector-CLI

![](https://raw.githubusercontent.com/kunal-mahatha/Vector-CLI/main/img/Vector-CLI.gif?token=APVZASYVYFGDNPZON4IRPTTA3YHNS)

## About the Tool
This is a CLI tool for operation on Vector Quantities.

## Features
 - Finds position vector from given two different points in a space.
 - Finds Magnitude of a Vector.
 - Finds Direction of a Vector.
 - Check whether the given two vectors are Perpendicular or not.
 
 ### Usage
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


[![MasterHead](https://raw.githubusercontent.com/kunal-mahatha/Vector-CLI/main/img/1.jpg?token=APVZAS7XM6H6IFDJKP7VHEDA3X3XO)](https://username.github.io)

  - Hit Enter to continue
  ```python
                
  ```



  ## Exploring the Menu Options
  
  [![MasterHead](https://raw.githubusercontent.com/kunal-mahatha/Vector-CLI/main/img/2.jpg?token=APVZAS276FUA2OK36REFPB3A3X334)](https://username.github.io)
  
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
   ## 3. Find if the vectors are perpendicular
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
   
   ## JFK ( Just for Knowledge )
   
   ### What is a scaler ?
   **A Scalar** or **Scalar Quantity** is a quantity that can be described by a single element of a number field, such as a real number, often accompanied by units of measurement
   
   ### What is a vector ?
   **A Vector** or **Vector Quantity** is a quantity that has both magnitude and direction. It is typically represented by an arrow whose direction is the same as that of the quantity and whose length is proportional to the quantity's magnitude. Although a vector has magnitude and direction, it does not have position.
