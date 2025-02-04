# Solving the Heat Equation Using the Finite Difference Method

## Introduction
This project involves solving the **heat equation** using the **finite difference method**. The program, written in **Python**, calculates and updates the temperature of a rod at each point over time. Finally, it plots the temperature variations over time.

## Equation Used

Heat Equation →
![image](https://github.com/user-attachments/assets/36aebd9f-52a3-4bb8-8f43-6a7140ca8261)

Initial Conditions →
![image](https://github.com/user-attachments/assets/96f288be-59d9-41f0-84c4-c79b69d739dc)

Boundary Conditions
1. ![image](https://github.com/user-attachments/assets/71ac909b-6eb9-4dd0-bef8-58eb1b434a89)
2. ![image](https://github.com/user-attachments/assets/278b6df5-32a9-4b1c-bab9-e3586a4711bf)

When this partial differential equation is solved, its solution is as follows:

![image](https://github.com/user-attachments/assets/7ed7fc2d-a846-442f-98cd-24e7fc46f0b6)

![image](https://github.com/user-attachments/assets/b0444669-d6d1-4d03-a33b-db092ac6ae0d)



## Implementation in Python
This program is written using **NumPy** for numerical calculations and **Matplotlib** for plotting.

### Key Sections of the Code:
1. **Creating the Temperature Array**
    ```python
    u = np.zeros(nx)
    u[int(0.4 * nx):int(0.6 * nx)] = 100
    ```
2. **Computing New Temperature Values**
    ```python
    for n in range(nt):
        for i in range(1, nx - 1):
            u_new[i] = u[i] + r * (u[i + 1] - 2 * u[i] + u[i - 1])
        u[:] = u_new
    ```
3. **Plotting Temperature Variations**
    ```python
    plt.plot(..., label=f"t = {n * dt:.2f} s")
    plt.show()
    ```

## Sample Output
The program plots the temperature distribution at each time step, showing how it evolves over time.

## Source
The images used for the equations are sourced from the following website:
Engineering Mathematics: Partial Differential Equations - Linom.org

