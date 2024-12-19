# CSV File Overview

## File Name: `data.csv`

### Description
`data.csv` contains critical data for the **Customer Segmentation and Recommendation System** project. It serves as the primary dataset for analysis, training, and evaluation of machine learning models.

### Structure
The CSV file is structured in the following format:

| Column Name      | Description                                      |
|------------------|--------------------------------------------------|
| `InvoiceNo`      | Unique identifier for each invoice              |
| `StockCode`      | Code representing the stock item                |
| `Description`    | Description of the stock item                   |
| `Quantity`       | Number of items purchased                       |
| `InvoiceDate`    | Date and time of the invoice                    |
| `UnitPrice`      | Price per unit of the stock item (in GBP)       |
| `CustomerID`     | Unique identifier for each customer             |
| `Country`        | Country of the customer                         |

### Usage
This dataset is used for:
1. **Customer Segmentation**: Clustering customers based on spending behavior and demographics.
2. **Recommendation System**: Predicting and recommending products or services.

### File Size
The dataset is approximately **45 MB** and is tracked using **Git LFS** to handle large file sizes efficiently.

### Sample Data
Here’s a preview of the first few rows of the dataset:

| InvoiceNo | StockCode | Description                        | Quantity | InvoiceDate       | UnitPrice | CustomerID | Country         |
|-----------|-----------|------------------------------------|----------|-------------------|-----------|------------|-----------------|
| 536365    | 85123A    | WHITE HANGING HEART T-LIGHT HOLDER | 6        | 12/1/2010 8:26   | 2.55      | 17850      | United Kingdom  |
| 536365    | 71053     | WHITE METAL LANTERN               | 6        | 12/1/2010 8:26   | 3.39      | 17850      | United Kingdom  |
| 536365    | 84406B    | CREAM CUPID HEARTS COAT HANGER    | 8        | 12/1/2010 8:26   | 2.75      | 17850      | United Kingdom  |
| 536365    | 84029G    | KNITTED UNION FLAG HOT WATER BOTTLE| 6        | 12/1/2010 8:26   | 3.39      | 17850      | United Kingdom  |
| 536365    | 84029E    | RED WOOLLY HOTTIE WHITE HEART.    | 6        | 12/1/2010 8:26   | 3.39      | 17850      | United Kingdom  |
| 536365    | 22752     | SET 7 BABUSHKA NESTING BOXES      | 2        | 12/1/2010 8:26   | 7.65      | 17850      | United Kingdom  |

### Important Notes
- Ensure Git LFS is installed and initialized before pulling the repository to avoid issues with the file.
- Use the following commands to fetch the file:
  ```bash
  git lfs pull
  ```

### Contact
For questions or issues with `data.csv`, please contact the repository maintainer or raise an issue in the GitHub repository.

