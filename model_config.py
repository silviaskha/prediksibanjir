import joblib

# IMPORT DICTIONARY KE APP.PY:
# from model_config import models_and_scalers  # Impor dictionary

# Load semua model dan scaler
try:
    model = joblib.load('model/knn_model_banjir.pkl')
    scaler = joblib.load('model/scaler_banjir.pkl')

    model2 = joblib.load('model/knn_model_nil.pkl')
    scaler2 = joblib.load('model/scaler_nil.pkl')

    # Tambahkan model dan scaler lainnya jika diperlukan
except FileNotFoundError:
    print("Error: File model atau scaler tidak ditemukan.")
    model, scaler = None, None
    model, scaler2 = None, None

# Dictionary mapping lokasi_id ke (model, scaler)
models_and_scalers = {
    1: {'model': model, 'scaler': scaler},
    2: {'model': model2, 'scaler': scaler2},
    # Tambahkan lokasi baru dengan model dan scaler lainnya
}
