from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier

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

def train_gbm(X_train, y_train):
    gbm = GradientBoostingClassifier(
    n_estimators=300,
    criterion='friedman_mse',
    max_depth=25,
    min_samples_split=3,
    min_samples_leaf=1,
    max_features='sqrt',
    random_state=42
    )

    gbm.fit(X_train, y_train)
    return gbm


