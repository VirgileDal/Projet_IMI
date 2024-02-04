import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.init as init
import torch.nn.functional as F

Kernel = 3
Padding = 1 #int((Kernel-1)/2)
Stride = 1

# self.encoder = nn.Sequential(
#     nn.Conv2d(1,64,Kernel,Stride,Padding),
#     nn.ReLU(True),
#     nn.MaxPool2d(2, 2),
#     nn.Conv2d(64,32,Kernel,Stride,Padding),
#     nn.ReLU(True),
#     nn.MaxPool2d(2, 2),
#     nn.Conv2d(32,16,Kernel,Stride,Padding),
#     nn.ReLU(True),
#     nn.MaxPool2d(2, 2),
#     nn.Conv2d(16,8,Kernel,Stride,Padding),
#     nn.ReLU(True),
#     nn.MaxPool2d(2, 2),
# )


# self.decoder = nn.Sequential(
#     nn.ConvTranspose2d(8,8,2,stride=2),
#     nn.ReLU(True),
#     nn.ConvTranspose2d(8,16,2,stride=2),
#     nn.ReLU(True),
#     nn.ConvTranspose2d(16,32,2,stride=2),
#     nn.ReLU(True),
#     nn.ConvTranspose2d(32,64,2,stride=2),
#     nn.ReLU(True),
#     nn.Conv2d(64,1,Kernel,Stride,Padding),
#     nn.Sigmoid()
# )

# iterate for each epoch
# for epoch in range(20):
    
#     lr = lr0 * lr_gamma**int(epoch/lr_step)
#     optimizer.lr = lr
#     print (lr)
    
#     losses = []
#     start = time.time()
    
#     for inputs, targets in tqdm.tqdm((trainingLoader)):
        
#         # inputs = inputs.view(inputs.size(0),-1).type(torch.FloatTensor)
#         # targets = targets.view(inputs.size(0),-1).type(torch.FloatTensor)
        
#         inputs = inputs.type(torch.FloatTensor)
#         targets = targets.type(torch.FloatTensor)
        
#         inputs, targets = inputs.to(device), targets.to(device)
        
#         optimizer.zero_grad()
#         outputs = net(inputs)

#         loss = criterion(outputs, targets)
        
#         # loss.requires_grad = True
#         loss.backward()
#         optimizer.step()
        
#         losses.append(loss.data.item())
#         lossesTRAll.append(loss.data.item())
    
#     end = time.time()
    
#     lossesTR.append(np.mean(losses))
#     idxEpoch.append(idxEpoch[-1] + len(losses))
#     print('Epoch : %d Train Loss : %.3f         time: %.3f' % (epoch, np.mean(losses),end-start))
    
    
#     # Evaluate the current network on the validation dataset
#     net.eval()
#     total = 0
#     correct = 0
#     losses = []
#     start = time.time()
    
#     for inputs, targets in tqdm.tqdm((testingLoader)):

#         # inputs = inputs.view(inputs.size(0),-1).type(torch.FloatTensor)
#         # targets = targets.view(targets.size(0),-1).type(torch.FloatTensor)
        
#         inputs = inputs.type(torch.FloatTensor)
#         targets = targets.type(torch.FloatTensor)
        
#         inputs, targets = inputs.to(device), targets.to(device)
    
#         outputs = net(inputs)
            
#         loss = criterion(outputs, targets)
        
#         losses.append(loss.data.item())
        
#         _, predicted = torch.max(outputs.data, 1)
        
#         total += targets.size(0)
#         correct += predicted.eq(targets.data).cpu().sum()
        
#     end = time.time()
#     lossesTE.append(np.mean(losses))
    
#     bestAcc = max(bestAcc,100.*correct/total)
#     print('Epoch : %d Test Loss  : %.3f        Test Acc %.3f       time: %.3f' % (epoch, np.mean(losses),100.*correct/total,end-start))
#     print('--------------------------------------------------------------')
#     net.train()