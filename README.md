# Google Maps Route Optimizer

This Python script uses Selenium to automate Google Maps to find an efficient route for visiting multiple destinations from a single starting point.

## 📋 Description

The script takes a predefined starting address and a list of destination addresses. It then programmatically calculates the distance from the start point to each destination, sorts them by proximity, and inputs this optimized order back into Google Maps to generate a multi-stop route. This is useful for planning deliveries, service calls, or any multi-destination trip efficiently.

## ✨ Features

  * Automates browser interaction with Selenium and `webdriver-manager`.
  * Accepts a fixed starting point and a list of destinations.
  * Calculates an optimized travel order by sorting destinations based on their distance from the start.
  * Automatically populates the multi-stop directions form on Google Maps.
  * Leaves the browser open with the final, optimized route displayed for review.

## ⚙️ How It Works

The script implements a simple heuristic to find an efficient path:

1.  It opens Google Maps and enters the starting location.
2.  It iterates through the list of destinations one by one, calculating the direct travel distance from the starting point to each.
3.  It sorts the destinations based on this distance, from nearest to farthest.
4.  Finally, it clears the destinations and re-enters them in the newly optimized order, creating the final multi-stop route.

## 🔧 Prerequisites

Before running the script, you need to have Python 3 and Google Chrome installed. You will also need to install the following Python libraries:

```bash
pip install selenium webdriver-manager
```

## ▶️ How to Use

1.  **Clone this repository** or save the `rotas.py` file to your local machine.

2.  **Install the dependencies:**

    ```bash
    pip install selenium webdriver-manager
    ```

3.  **Edit the Script:** Open the `rotas.py` file and modify the following variables at the bottom of the script with your desired addresses:

      * `startpoint`: Set your single starting address.
      * `enderecos`: Fill this list with all the destination addresses you need to visit.

4.  **Run the Script:** Execute the script from your terminal:

    ```bash
    python rotas.py
    ```

A new Chrome window will open and perform all the steps automatically. The process may take a minute depending on your internet connection. The script will leave the browser window open with the final, optimized route displayed on Google Maps.

-----

**Disclaimer:** This script depends on the specific HTML structure (IDs and XPaths) of the Google Maps website. If Google updates its site, the element selectors in the script may need to be updated to function correctly.
