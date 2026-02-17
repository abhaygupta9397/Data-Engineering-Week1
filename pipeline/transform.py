def transform(df):
    df = df.dropna()
    return df.groupby("city")["amount"].sum().reset_index()
