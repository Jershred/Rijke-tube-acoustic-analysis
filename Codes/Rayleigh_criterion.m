%Combustion for propulstion - BE 2 (Rijke tube)

%Parameters
L=1.783; %Length of the tube
n=0.01; %Normalized flame response
c1= 340; %Speed of sound in the first part of the tube
c2=2*c1; %Speed of sound in the second part of the tube
rho1=1.2; %Air density in the first part of the tube
rho2=rho1/4; %Air density in the second part of the tube
r=0.2; %Position of the flame
U0=20; %Mean speed of the flow
tau=r/U0; 

%Question 4 : Plotting the structure of the standing pressure inside the
%tube

f1=[93.5,1046.9,2000.4,2953.8,3907.3,4860.7,5814.2,6767.6,7721.1,8674.5,9628.0]; %Frequency considered
omega=2*pi*f1; 
k1=omega/c1;
k2=omega/c2;
L1=r*L;
x1=linspace(0,r*L,1000);
x2=linspace(r*L,L,1000);
X=[x1,x2];

% p1_1=2*cos(k1(1)*x1);
% phase1_1=angle(p1_1);
% p2_1exp=1i*exp(-1i*k2(1)*(L-L1))*(cos(k1(1)*L1)/sin(k2(1)*(L-L1)))*(exp(1i*k2(1)*(x2-L1))-exp(-1i*k2(1)*(x2-L1))*exp(2*1i*k2(1)*(L-L1)));
% phase2_1=angle(p2_1exp);
% p2_1=abs(p2_1exp);
% P1=[p1_1,p2_1];
% phase1=[phase1_1,phase2_1];
% 
% p1_2=2*cos(k1(2)*x1);
% phase1_2=angle(p1_2);
% p2_2exp=1i*exp(-1i*k2(2)*(L-L1))*(cos(k1(2)*L1)/sin(k2(2)*(L-L1)))*(exp(1i*k2(2)*(x2-L1))-exp(-1i*k2(2)*(x2-L1))*exp(2*1i*k2(2)*(L-L1)));
% phase2_2=angle(p2_2exp);
% p2_2=abs(p2_2exp);
% P2=[p1_2,p2_2];
% phase2=[phase1_2,phase2_2];
% 
% p1_3=2*cos(k1(3)*x1);
% phase1_3=angle(p1_3);
% p2_3exp=1i*exp(-1i*k2(3)*(L-L1))*(cos(k1(3)*L1)/sin(k2(3)*(L-L1)))*(exp(1i*k2(3)*(x2-L1))-exp(-1i*k2(3)*(x2-L1))*exp(2*1i*k2(3)*(L-L1)));
% phase2_3=angle(p2_3exp);
% p2_3=abs(p2_3exp);
% P3=[p1_3,p2_3];
% phase3=[phase1_3,phase2_3];
% 
% p1_4=2*cos(k1(4)*x1);
% phase1_4=angle(p1_4);
% p2_4exp=1i*exp(-1i*k2(4)*(L-L1))*(cos(k1(4)*L1)/sin(k2(4)*(L-L1)))*(exp(1i*k2(4)*(x2-L1))-exp(-1i*k2(4)*(x2-L1))*exp(2*1i*k2(4)*(L-L1)));
% phase2_4=angle(p2_4exp);
% p2_4=abs(p2_4exp);
% P4=[p1_4,p2_4];
% phase4=[phase1_4,phase2_4];
%plot(X,P1,'b',X,P2,'r',X,P3,'g',X,P4,'m');
%plot(X,phase1,'b',X,phase2,'r',X,phase3,'g',X,phase4,'m');

% p1_5=2*cos(k1(5)*x1);
% phase1_5=angle(p1_5);
% p2_5exp=1i*exp(-1i*k2(5)*(L-L1))*(cos(k1(5)*L1)/sin(k2(5)*(L-L1)))*(exp(1i*k2(5)*(x2-L1))-exp(-1i*k2(5)*(x2-L1))*exp(2*1i*k2(5)*(L-L1)));
% phase2_5=angle(p2_5exp);
% p2_5=abs(p2_5exp);
% P5=[p1_5,p2_5];
% phase5=[phase1_5,phase2_5];
% 
% p1_6=2*cos(k1(6)*x1);
% phase1_6=angle(p1_6);
% p2_6exp=1i*exp(-1i*k2(6)*(L-L1))*(cos(k1(6)*L1)/sin(k2(6)*(L-L1)))*(exp(1i*k2(6)*(x2-L1))-exp(-1i*k2(6)*(x2-L1))*exp(2*1i*k2(6)*(L-L1)));
% phase2_6=angle(p2_6exp);
% p2_6=abs(p2_6exp);
% P6=[p1_6,p2_6];
% phase6=[phase1_6,phase2_6];
% 
% p1_7=2*cos(k1(7)*x1);
% phase1_7=angle(p1_7);
% p2_7exp=1i*exp(-1i*k2(7)*(L-L1))*(cos(k1(7)*L1)/sin(k2(7)*(L-L1)))*(exp(1i*k2(7)*(x2-L1))-exp(-1i*k2(7)*(x2-L1))*exp(2*1i*k2(7)*(L-L1)));
% phase2_7=angle(p2_7exp);
% p2_7=abs(p2_7exp);
% P7=[p1_7,p2_7];
% phase7=[phase1_7,phase2_7];
% 
% p1_8=2*cos(k1(8)*x1);
% phase1_8=angle(p1_8);
% p2_8exp=1i*exp(-1i*k2(8)*(L-L1))*(cos(k1(8)*L1)/sin(k2(8)*(L-L1)))*(exp(1i*k2(8)*(x2-L1))-exp(-1i*k2(8)*(x2-L1))*exp(2*1i*k2(8)*(L-L1)));
% phase2_8=angle(p2_8exp);
% p2_8=abs(p2_8exp);
% P8=[p1_8,p2_8];
% phase8=[phase1_8,phase2_8];
% plot(X,P5,'b',X,P6,'r',X,P7,'g',X,P8,'m');
% plot(X,phase5,'b',X,phase6,'r',X,phase7,'g',X,phase8,'m');

p1_9=2*cos(k1(9)*x1);
phase1_9=angle(p1_9);
p2_9exp=1i*exp(-1i*k2(9)*(L-L1))*(cos(k1(9)*L1)/sin(k2(9)*(L-L1)))*(exp(1i*k2(9)*(x2-L1))-exp(-1i*k2(9)*(x2-L1))*exp(2*1i*k2(9)*(L-L1)));
phase2_9=angle(p2_9exp);
p2_9=abs(p2_9exp);
P9=[p1_9,p2_9];
phase9=[phase1_9,phase2_9];

p1_10=2*cos(k1(10)*x1);
phase1_10=angle(p1_10);
p2_10exp=1i*exp(-1i*k2(10)*(L-L1))*(cos(k1(10)*L1)/sin(k2(10)*(L-L1)))*(exp(1i*k2(10)*(x2-L1))-exp(-1i*k2(10)*(x2-L1))*exp(2*1i*k2(10)*(L-L1)));
phase2_10=angle(p2_10exp);
p2_10=abs(p2_10exp);
P10=[p1_10,p2_10];
phase10=[phase1_10,phase2_10];

p1_11=2*cos(k1(11)*x1);
phase1_11=angle(p1_11);
p2_11exp=1i*exp(-1i*k2(11)*(L-L1))*(cos(k1(11)*L1)/sin(k2(11)*(L-L1)))*(exp(1i*k2(11)*(x2-L1))-exp(-1i*k2(11)*(x2-L1))*exp(2*1i*k2(11)*(L-L1)));
p2_11=abs(p2_11exp);
phase2_11=angle(p2_11exp);
P11=[p1_11,p2_11];
phase11=[phase1_11,phase2_11];

%plot(X,P9,'b',X,P10,'r',X,P11,'g');
plot(X,phase9,'b',X,phase10,'r',X,phase11,'g');




