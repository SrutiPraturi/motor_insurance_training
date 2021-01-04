import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error as mse
from sklearn.metrics import r2_score
import yaml
import numpy as np
import pickle 

class ModelTrain:

    def load_data(self,data):
        data = pd.read_csv(data)
    
        return data 

    def train_model(self,data):
        x=data.drop(['Payment'],axis =1)
        y=data['Payment']


        x_train , x_test , y_train , y_test = train_test_split(x,y, test_size = 0.2 , random_state = 42)
    
        x_train.to_csv('datasets/insurance_model_features.csv',index = False)
    
    

        model = LinearRegression().fit(x_train , y_train)
        training_RMSE = np.sqrt(mse(np.expm1(y_train) , np.expm1(model.predict(x_train))))
        test_RMSE = np.sqrt(mse(np.expm1(y_test), np.expm1(model.predict(x_test))))
    
        model_r2 = r2_score(y_test,model.predict(x_test))
    
        features = x_train.columns
    
        final_data = x_train
        final_data = final_data.assign(Payment = y_train)
    
        final_data.to_csv('datasets/insurance_data.to_csv',index = False)
    
    
    
        d = {'features' : list(features) , 'training_RMSE': float(training_RMSE), 'test_RMSE': float(test_RMSE) , 'Model R2' : float(model_r2)}
    
        file = open('assets/claims_model.pkl','wb')
        pickle.dump(model , file)
        file.close()
    
        with open('assets/baseline.yaml', 'w') as yaml_file:
            yaml.dump(d, yaml_file, default_flow_style=False)
        
if __name__ == "__main__":
    modeltrain = ModelTrain()
    data= modeltrain.load_data('assets/insurance_processed_data.csv')
    modeltrain.train_model(data)
