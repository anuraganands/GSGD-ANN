import numpy as np
import pandas as pd
import torch
import torchmetrics
import copy
from getError import *
thisdevice = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

def validate(inputVal, network, actual, loss_function):
    xval = inputVal.to(device = thisdevice)
    actual = actual.to(device = thisdevice)
    
    #get predicted value
    predicted = get_predictions(network, xval)
    
    SR = torchmetrics.functional.accuracy(predicted, actual)
    loss = loss_function(predicted, actual)
    E = loss.item()   
    return SR, E  

# Calculate accuracy percentage
def accuracy_metric(actual, predicted):
	correct = 0
	for i in range(len(actual)):
		if actual[i][0] == torch.round(predicted[i][0]).float():
			correct += 1
	return correct

def get_predictions(network, xts):
    network.zero_grad()
    pred_y = network(xts)
    return pred_y
