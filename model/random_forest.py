from sklearn.ensemble import RandomForestClassifier

def train_random_forest(X_train, y_train):
    rf_model = RandomForestClassifier(
        n_estimators=200,
        criterion='entropy',
        max_depth=20,
        min_samples_split=5,
        min_samples_leaf=2,
        max_features='log2',
        random_state=42
    )
    rf_model.fit(X_train, y_train)
    return rf_model
