# MIT 6.100L : Problem Set 1

This repository contains the complete implementation for **Problem Set 1**, which focuses on basic Python expressions, control flow (while loops, conditionals), user input processing, and numerical approximation using **Bisection Search**.

---

## Project Structure

* **`ps1a.py` (Part A):** Implementation of a basic financial tracking script to calculate the time required to save for a down payment.
* **`ps1b.py` (Part B):** An extended version of the savings script that incorporates a semi-annual salary raise mechanism.
* **`ps1c.py` (Part C):** An algorithmic solution that uses bisection search to find the optimal savings rate required to achieve a financial goal within a strict timeframe.

---

## Detailed Components

### Part A: House Hunting

* **Savings Tracking**: Simulates monthly financial growth by taking user inputs for annual salary, percentage of salary to save, and the total cost of a dream home.
* **Investment Returns**: Factors in a compound monthly return on existing savings based on an annual investment return rate (defaulted to $4\%$). It determines the exact number of months needed to reach a $25\%$ down payment.

### Part B: Saving, with a Raise

* **Dynamic Salary Escalation**: Modifies the Part A loop to account for professional growth. It introduces a semi-annual raise percentage input. Every 6 months, the baseline annual salary automatically increases, adjusting the monthly savings contribution dynamically.

### Part C: Finding the Right Savings Rate (Bisection Search)

* **Algorithmic Optimization**: Instead of calculating time based on a fixed rate, this part fixes the timeframe to exactly **36 months** and searches for the ideal savings rate.
* **Bisection Search Implementation**: Rather than brute-forcing through 10,000 possible rates (from $0\%$ to $100\%$), it uses binary search mechanics to locate the rate within a small margin of error ($\pm \$100$ of the required down payment) in $O(\log N)$ steps.
* **Feasibility Check**: Safely detects and reports if the target down payment is fundamentally impossible to reach within 36 months, even with a $100\%$ savings rate.

---

## Important Constraints & Style Guidelines

* **Floating-Point Precision**: Floating-point numbers are used for financial growth rates. When evaluating the bisection search termination condition, the algorithm checks if the absolute difference is within an epsilon value rather than searching for an exact float match:

$$\left\vert{} \text{Current Savings} - \text{Target Down Payment} \right\vert{} \le 100$$


* **Integer Steps**: The bisection search operates on an integer search space (e.g., $0$ to $10000$) to represent percentages accurately up to four decimal places ($0.00\%$ to $100.00\%$), preventing floating-point iteration issues.
* **Loop Efficiency**: The search loop tracks and outputs the exact number of bisection steps taken to demonstrate the efficiency of the binary search pattern compared to linear checking.

---

## Testing

This problem set is verified manually using the test cases provided in the assignment documentation. You can test each script by running them in your terminal and providing the requested test inputs:

```bash
python ps1a.py
python ps1b.py
python ps1c.py

```