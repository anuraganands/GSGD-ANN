import numpy as np
from validateSet import *
import matplotlib.pyplot as plt
            
def print_results_final(inputVal, network, actual, loss_function, type = ''):
    xval = inputVal
    
    #get predicted value
    predicted = get_predictions(network, xval)
    
    accuracy = torchmetrics.functional.accuracy(predicted, actual)
    loss = loss_function(predicted, actual)
    overall_E = loss.item()
    recall = torchmetrics.functional.recall(preds=predicted, target=actual)
    precision = torchmetrics.functional.precision(preds=predicted, target=actual)
    specifity = torchmetrics.functional.specificity(preds=predicted, target=actual)
    f1score = torchmetrics.functional.f1_score(preds=predicted, target=actual)
    fpr, tpr, thresholds =  torchmetrics.functional.roc(preds=predicted, target=actual)
    precision_plot, recall_plot, thresholds_prc =  torchmetrics.functional.precision_recall_curve(preds=predicted, target=actual)

    print('\n\n--Results------'+ type)
    print('Classification Accuracy: ', accuracy.item())
    print('overall Error', overall_E)
    print('Recall: ', recall.item())
    print('Precision: ', precision.item())
    print('Specificity: ', specifity.item())
    print('F1-score: ', f1score.item())
    print('----------------')

    #ROC Curve
    plt.figure()
    plt.plot([0.0, 1.0], [0.0, 1.0], linestyle='--')
    plt.plot(fpr.cpu().data.numpy(), tpr.cpu().data.numpy(),'g--', label='ROC', marker='.', markersize='0.02')
    plt.title('ROC Curve')
    plt.ylabel('True Positive Rate')
    plt.xlabel('False Positive Rate')
    #plt.savefig('graphs/'+ type +'/roc_curve.png')
    plt.show()
    
    #precision Recall Curve
    no_skill = len(actual[actual==1]) / len(actual)
    plt.figure()
    plt.plot([0.0, 1.0], [no_skill,no_skill], linestyle='--')
    plt.plot(recall_plot.cpu().data.numpy(), precision_plot.cpu().data.numpy(),'g--', label='Precision-Recall Curve', marker='.', markersize='0.02')
    plt.title('Precision Recall Curve')
    plt.ylabel('Precision')
    plt.xlabel('Recall')
    #plt.savefig('graphs/'+ type +'/Precision_recall_curve.png')
    plt.show()

def generate_graphs(epochs, results_container):
    GSGD_SRoverEpochs, GSGD_EoverEpochs, SGD_SRoverEpochs, SGD_EoverEpochs = results_container

    Epocperm = [ i+1 for i in range(epochs)]

    # Error Convergence of GSGD and SGD
    plt.figure()
    plt.plot(Epocperm, SGD_EoverEpochs, label='SGD Error', linewidth=1)
    plt.plot(Epocperm, GSGD_EoverEpochs, 'r--', label='GSGD Error', linewidth=1)

    plt.title('Error Convergence of GSGD and SGD')
    plt.xlabel("Epochs")
    plt.ylabel("Error")
    plt.legend(loc=2)

    #plt.savefig('graphs/error_convergence_general.png')
    plt.show()

    #Success rate GSGD and SGD over Epochs General
    plt.figure()
    plt.plot(Epocperm, SGD_SRoverEpochs, label='SGD SR', linewidth=1)
    plt.plot(Epocperm, GSGD_SRoverEpochs, 'r--', label='GSGD SR', linewidth=1)

    plt.title('Classification Accuracy of GSGD and SGD')
    plt.xlabel("Epochs")
    plt.ylabel("Classification Accuracy")
    plt.legend(loc=2)

    #plt.savefig('graphs/success_rate_general.png')
    plt.show()