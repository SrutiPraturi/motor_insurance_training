import pandas as pd 
import numpy as np
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import GridSearchCV
from sklearn.preprocessing import MinMaxScaler
from sklearn.cluster import KMeans
import pickle
import os


class DataPipeline:

    def load_data(self,data_path):
        data = pd.read_csv(data_path)
    
        return data

    def treat_data(self,data):
        #removing claims = 0 , payment = 0 
        data = data[data['Payment'] != 0]
        #removing payment > 1000000 as outliers
        data = data[data['Payment'] <= 1000000]
        data['Payment'] = np.log1p(data['Payment'])
    
        return data

    def feature_engg(self,data) :
    
        train = data[['Claims','Insured','Payment']]
        x=train.drop('Payment',axis =1)
        y=train['Payment']
        x_train , x_test , y_train , y_test = train_test_split(x,y, test_size = 0.2 , random_state = 42)

        param_grid = {
                 'n_estimators': range(10,110,10),
                 'max_depth': range(2,10)
             }

        clf = RandomForestRegressor()
        grid_clf = GridSearchCV(clf, param_grid, cv=10)
        grid_clf.fit(x_train, y_train)
        data['PLS'] = grid_clf.predict(data[['Claims','Insured']])
    
        #store the trained model object for feature engineering
        file = open('assets/RFR_claims_insured.pkl','wb')
        pickle.dump(grid_clf,file)
        file.close()
    
    
    def store_data(self,data):
        data.to_csv('datasets/insurance_treated_data.csv',index = False)
    
if __name__ == "__main__":
    datapipeline = DataPipeline()
    os.mkdir('assets')
    os.mkdir('datasets')
    data = datapipeline.load_data('SwedishMotorInsurance.csv')
    datapipeline.data_treated = treat_data(data)
    datapipeline.feature_engg(data_treated)
    datapipeline.store_data(data_treated)
    
    

