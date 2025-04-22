
import re
import pandas as pd
import matplotlib.pyplot as plt

# 1. Configuration 
INPUT_CSV        = 'DistributorsData.csv'   
CLEANED_CSV      = 'cleaned_list.csv'
INVALID_CSV      = 'invalid_list.csv'
PHONE_REGEX      = r'^[935]\d{9}$'          

#  2. Validation Functions 
def valid_phone(x: str) -> bool:
    """Phone must be 10 digits starting with 9, 3, or 5."""
    return bool(re.match(PHONE_REGEX, str(x).strip()))

def valid_gender(x: str) -> bool:
    """Gender must be one of M, F, or O (case‑insensitive)."""
    return str(x).strip().upper() in {'M', 'F', 'O'}

def valid_age(x) -> bool:
    """Age must be an integer between 5 and 100."""
    try:
        age = int(x)
        return 5 <= age <= 100
    except (ValueError, TypeError):
        return False

# 3. Load Data 
df = pd.read_csv(INPUT_CSV)

# 4. Apply Validations 
mask_phone  = df['Phone' ].apply(valid_phone)
mask_gender = df['Gender'].apply(valid_gender)
mask_age    = df['Age'   ].apply(valid_age)

valid_mask  = mask_phone & mask_gender & mask_age
clean_df    = df[valid_mask].copy()
invalid_df  = df[~valid_mask].copy()

# 5. Save Outputs 
clean_df.to_csv(CLEANED_CSV, index=False)
invalid_df.to_csv(INVALID_CSV, index=False)

# 6. Summary Statistics 
num_clean    = len(clean_df)
num_invalid  = len(invalid_df)
per_state    = clean_df['State'].value_counts().sort_index()
avg_age_st   = clean_df.groupby('State')['Age'].mean().round(2)
avg_age_all  = clean_df['Age'].mean().round(2)

# 7. Print Summary 
print(f" Clean entries:   {num_clean}")
print(f" Invalid entries: {num_invalid}\n")

print(" People per state:")
print(per_state.to_string(), "\n")

print(" Average age per state:")
print(avg_age_st.to_string(), "\n")

print(f" Average age overall: {avg_age_all}\n")

# 8. Visualization 
plt.figure(figsize=(8,5))
per_state.plot(kind='bar')
plt.title("Number of People per State")
plt.xlabel("State")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("people_per_state.png")  # also save the figure
plt.show()


