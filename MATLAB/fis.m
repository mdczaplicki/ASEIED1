% set number of classes
clusters = 20;

% uncomment file you want to load
%fcmdata = load('a2.txt');
fcmdata = load('yeast.txt');

% find class for all points
[centers, U] = fcm(fcmdata, clusters);
maxU = max(U);

% match every point to a class
index = [];
for i = 1:clusters
    temp = find(U(i,:) == maxU);
    index(i).indexes = temp;
end

figure()
hold on
% generate table of unrepeatable colors
cmap = hsv(clusters);

% for every class plot it and scatter every point that belongs to it
for i = 1:clusters
    scatter(fcmdata(index(i).indexes, 1), fcmdata(index(i).indexes, 2),25,cmap(i,:));
    plot(centers(i, 1), centers(i, 2), '+', 'MarkerSize', 25, 'LineWidth',10, 'Color', 'black');
    plot(centers(i, 1), centers(i, 2), '+', 'MarkerSize', 15, 'LineWidth',3, 'Color',cmap(i,:));
end