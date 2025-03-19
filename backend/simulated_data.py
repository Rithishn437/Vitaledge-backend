# Simulated dataset for blood parameters and conditions
simulated_dataset = [
    # Normal (Male, Adult)
    [14.5, 5.2, 6000, 200000, "Normal"],  # Healthy adult male
    [15.0, 5.0, 7500, 250000, "Normal"],
    [13.8, 4.8, 8000, 300000, "Normal"],
    [16.0, 5.5, 9000, 350000, "Normal"],  # High normal
    [13.5, 4.7, 7000, 280000, "Normal"],
    
    # Normal (Female, Adult)
    [13.0, 4.5, 6500, 220000, "Normal"],  # Healthy adult female
    [12.5, 4.3, 7000, 280000, "Normal"],
    [14.0, 4.7, 7200, 260000, "Normal"],
    [12.8, 4.2, 6800, 240000, "Normal"],
    [14.5, 4.9, 8000, 270000, "Normal"],
    
    # Anemia (Male, Low Hemoglobin/RBC)
    [11.0, 3.8, 5000, 180000, "Anemia"],  # Mild anemia
    [10.5, 3.5, 4500, 150000, "Anemia"],  # Moderate anemia
    [9.8, 3.2, 4800, 140000, "Anemia"],   # Severe anemia
    [12.0, 4.0, 5500, 200000, "Anemia"],  # Borderline anemia
    [11.5, 4.2, 6000, 190000, "Anemia"],
    
    # Anemia (Female, Low Hemoglobin/RBC)
    [10.0, 3.7, 6000, 160000, "Anemia"],  # Mild anemia
    [9.5, 3.4, 5200, 130000, "Anemia"],   # Moderate anemia
    [11.5, 4.0, 5800, 190000, "Anemia"],  # Borderline anemia
    [10.5, 3.9, 6200, 170000, "Anemia"],
    [9.0, 3.5, 5500, 150000, "Anemia"],   # Severe anemia
    
    # Infection (High WBC, Male/Female)
    [14.0, 5.0, 12000, 300000, "Infection"],  # High WBC
    [13.5, 4.8, 13000, 350000, "Infection"],
    [12.5, 4.5, 11000, 280000, "Infection"],
    [15.0, 5.2, 15000, 400000, "Infection"],
    [14.5, 5.1, 12000, 310000, "Infection"],
    
    # Normal (Children, Age < 18, Adjusted Ranges: Hemoglobin Male 12.0-16.0, Female 11.0-14.0)
    [12.5, 4.7, 7000, 250000, "Normal"],  # Healthy child (male, <18)
    [12.0, 4.5, 6800, 270000, "Normal"],  # Healthy child (male, <18)
    [11.5, 4.3, 6500, 230000, "Normal"],  # Healthy child (female, <18) - FIXED: 11.5 is "Normal" (range 11.0-14.0)
    [13.0, 4.8, 7200, 260000, "Normal"],
    [11.8, 4.4, 6900, 240000, "Normal"],
    
    # Anemia (Children, Age < 18)
    [9.0, 3.0, 5000, 160000, "Anemia"],   # Child with anemia (male)
    [8.5, 2.9, 4800, 150000, "Anemia"],   # Child with anemia (female)
    [10.0, 3.5, 5200, 170000, "Anemia"],
    [7.5, 2.7, 4500, 140000, "Anemia"],   # Severe anemia (child, male)
    [8.0, 3.0, 4700, 130000, "Anemia"],   # Severe anemia (child, female)
    
    # Infection (Children, Age < 18)
    [11.5, 4.2, 14000, 320000, "Infection"],  # Child with infection
    [12.0, 4.4, 13000, 290000, "Infection"],
    [11.8, 4.3, 14000, 310000, "Infection"],
    
    # Edge Cases (Rare but Possible)
    [16.5, 5.8, 9000, 450000, "Normal"],  # High normal for male
    [15.5, 5.5, 9500, 420000, "Normal"],  # High normal for female
    [8.0, 2.8, 4000, 120000, "Anemia"],   # Severe anemia
    [14.0, 4.9, 16000, 500000, "Infection"],  # Very high WBC
    [12.8, 4.6, 8500, 340000, "Normal"],  # Balanced case
    
    # Additional Normal Cases
    [13.2, 4.7, 7200, 240000, "Normal"],
    [14.2, 5.1, 6800, 260000, "Normal"],
    [12.7, 4.4, 7300, 230000, "Normal"],
    [13.9, 4.9, 6900, 280000, "Normal"],
    [14.0, 5.0, 7500, 260000, "Normal"],
    [13.5, 4.8, 7200, 250000, "Normal"],
    [15.2, 5.3, 8000, 280000, "Normal"],
    [13.0, 4.6, 7300, 240000, "Normal"],
    [12.8, 4.4, 6800, 230000, "Normal"],
    [14.5, 4.9, 7900, 270000, "Normal"],
    
    # Additional Anemia Cases
    [10.8, 3.6, 5100, 170000, "Anemia"],
    [11.2, 3.9, 5300, 190000, "Anemia"],
    [9.7, 3.3, 4700, 140000, "Anemia"],
    [11.0, 4.2, 6800, 240000, "Anemia"],
    [10.8, 4.0, 6500, 230000, "Anemia"],
    [9.5, 3.7, 6200, 210000, "Anemia"],
    [11.2, 4.1, 7100, 220000, "Anemia"],
    [10.0, 3.8, 6900, 200000, "Anemia"],
    [9.8, 3.6, 6400, 190000, "Anemia"],
    
    # Additional Infection Cases
    [13.0, 4.8, 12500, 330000, "Infection"],
    [14.5, 5.3, 14500, 380000, "Infection"],
    [12.3, 4.6, 11500, 310000, "Infection"],
    [13.0, 4.7, 13000, 350000, "Infection"],
    [12.5, 4.5, 11500, 320000, "Infection"],
    
    # Mixed Cases (Borderline and Combined)
    [12.0, 4.2, 9000, 250000, "Normal"],  # Slightly low hemoglobin, normal overall
    [11.8, 4.1, 10000, 270000, "Anemia"],  # Borderline anemia
    [13.7, 5.0, 11000, 290000, "Normal"],  # Slightly high WBC, normal overall
    [14.2, 5.4, 13500, 360000, "Infection"],  # High WBC, infection likely
    
    # New Entries (30 Additional Samples)
    # More Normal Cases (Male/Female, Adults/Children)
    [15.5, 5.4, 8500, 320000, "Normal"],  # Male adult
    [13.2, 4.6, 7400, 260000, "Normal"],  # Female adult
    [12.8, 4.8, 7100, 270000, "Normal"],  # Male child (<18)
    [11.7, 4.3, 6800, 250000, "Normal"],  # Female child (<18)
    [14.0, 5.1, 7800, 290000, "Normal"],  # Male adult
    [12.9, 4.5, 7000, 240000, "Normal"],  # Female adult
    
    # More Anemia Cases (Severe and Combined)
    [7.8, 2.5, 4800, 130000, "Anemia"],   # Severe anemia (male adult)
    [8.2, 2.8, 5000, 140000, "Anemia"],   # Severe anemia (female adult)
    [7.0, 2.4, 4500, 120000, "Anemia"],   # Very severe anemia (child, male)
    [10.5, 3.8, 12000, 200000, "Anemia"],  # Anemia with high WBC (possible infection, male)
    [9.8, 3.5, 13000, 180000, "Anemia"],  # Anemia with high WBC (possible infection, female)
    [11.0, 4.0, 6000, 160000, "Anemia"],  # Mild anemia (female)
    
    # More Infection Cases (Severe and Combined)
    [14.8, 5.2, 17000, 400000, "Infection"],  # Severe infection (male adult)
    [13.5, 4.8, 18000, 380000, "Infection"],  # Severe infection (female adult)
    [12.0, 4.5, 16000, 350000, "Infection"],  # Severe infection (child, male)
    [11.5, 4.2, 15500, 340000, "Infection"],  # Severe infection (child, female)
    [10.8, 3.9, 14000, 310000, "Infection"],  # Infection with low hemoglobin (possible anemia, male)
    [9.5, 3.6, 15000, 300000, "Infection"],  # Infection with low hemoglobin (possible anemia, female)
    
    # More Borderline and Mixed Cases
    [12.9, 4.4, 11000, 290000, "Normal"],  # Borderline high WBC, normal overall (female)
    [13.1, 4.9, 11500, 300000, "Infection"],  # Slightly high WBC, infection likely (male)
    [11.9, 4.0, 10000, 280000, "Anemia"],  # Borderline anemia (female)
    [12.1, 4.6, 9000, 260000, "Normal"],  # Slightly low hemoglobin, normal overall (male child)
    [11.0, 4.1, 12000, 270000, "Anemia"],  # Anemia with high WBC (female child)
    
    # Additional Edge Cases
    [17.0, 5.9, 10000, 450000, "Normal"],  # Upper limit normal (male adult)
    [15.0, 5.1, 11000, 400000, "Normal"],  # Upper limit normal (female adult)
    [6.5, 2.2, 4000, 100000, "Anemia"],   # Very severe anemia (male adult)
    [14.0, 5.0, 20000, 500000, "Infection"],  # Extremely high WBC (male adult)
    [13.5, 4.8, 19000, 480000, "Infection"],  # Extremely high WBC (female adult)
    [10.0, 3.5, 17000, 320000, "Anemia"],  # Severe anemia with infection (child, male)
    [9.0, 3.2, 16000, 310000, "Anemia"],  # Severe anemia with infection (child, female)
]

# Total: 100 entries