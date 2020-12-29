import numpy as np
from sklearn.model_selection import KFold
from sklearn.tree import DecisionTreeRegressor

def get_features_targets(data):
  return np.hstack([
    (data[b1] - data[b2]).reshape(-1,1) 
    for b1, b2 in zip("ugri", "griz")
  ]), data['redshift']

# paste your median_diff function here
def median_diff(predicted, actual):
  return np.median(np.abs(predicted - actual))

# paste your cross_validate_model function here
def cross_validate_model(model, features, targets, k) :
  kf = KFold(n_splits=k, shuffle=True)
  all_predictions = np.zeros_like(targets)

  for train_indices, test_indices in kf.split(features):
    train_features, train_targets = features[train_indices], targets[train_indices]
    test_features= features[test_indices]
    dtr = DecisionTreeRegressor(max_depth=19)
    dtr.fit(train_features, train_targets)
    predictions = dtr.predict(test_features)
    all_predictions[test_indices] = predictions
    
  return all_predictions 

# complete this function
def split_galaxies_qsos(data):
  # split the data into galaxies and qsos arrays
  galbool = data['spec_class'] == b'GALAXY'

  # return the seperated galaxies and qsos arrays
  return data[galbool], data[np.invert(galbool)]
  
def cross_validate_median_diff(data) :
  features, targets = get_features_targets(data)
  return median_diff(cross_validate_model(DecisionTreeRegressor(max_depth=19), features, targets, 10), targets)

if __name__ == "__main__":
    data = np.load('./sdss_galaxy_colors.npy')

    # Split the data set into galaxies and QSOs
    galaxies, qsos= split_galaxies_qsos(data)

    # Here we cross validate the model and get the cross-validated median difference
    # The cross_validated_med_diff function is in "written_functions"
    galaxy_med_diff = cross_validate_median_diff(galaxies)
    qso_med_diff = cross_validate_median_diff(qsos)

    # Print the results
    print("Median difference for Galaxies: {:.3f}".format(galaxy_med_diff))
    print("Median difference for QSOs: {:.3f}".format(qso_med_diff))

