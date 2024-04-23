import pickle

loaded_model = pickle.load(open('trained_model.sav' , 'rb'))
loaded_vect = pickle.load(open('Vect.pickle' , 'rb'))
INP = input()
x_new = loaded_vect.transform([INP])

prediction = loaded_model.predict(x_new)

if(prediction == 0):
    print('Negative tweet')
else:
    print('Positive tweet')