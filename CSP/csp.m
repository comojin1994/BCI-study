function csp()
    channel = 100;
    sampling = 200;
    trials = 100;
    
    class_1 = normrnd(0, 1, [sampling, channel, trials]);
    class_2 = normrnd(2, 1, [sampling, channel, trials]);
    
    for i = 1:trials
        C1_covariance(:,:,i) = (class_1(:,:,i)' * class_1(:,:,i)) / trace(class_1(:,:,i)' * class_1(:,:,i)); % (X*X') / tr(X*X')
        C2_covariance(:,:,i) = (class_2(:,:,i)' * class_2(:,:,i)) / trace(class_2(:,:,i)' * class_2(:,:,i)); % (X*X') / tr(X*X')
    end
    
    mean_C1_cov = mean(C1_covariance, 3);
    mean_C2_cov = mean(C2_covariance, 3);
    
    C_sum = mean_C1_cov + mean_C2_cov;
    
    [EVecsum, EValsum] = eig(C_sum);
    [EValsum, ind] = sort(diag(EValsum), 'descend');
    EVecsum = EVecsum(:, ind);
    Q = zeros(channel, channel);
    Q = sqrt(pinv(diag(EValsum))) * EVecsum';
    
    S1 = Q * mean_C1_cov * Q';
    S2 = Q * mean_C2_cov * Q';
    
    [B, D] = eig(S1, S2);
    [D, ind] = sort(diag(D));
    B = B(:, ind);
    CSP_filter = zeros(channel, channel);
    
    CSP_filter = B' * Q;
    
    m = 2;
    sel_CSP_filter(1:m, :) = CSP_filter(1:m,:);
    sel_CSP_filter(m+1:2*m, :) = CSP_filter(channel - (m-1):channel,:);
    
    for i = 1: trials
        trans_signal_C1(:,:,i) = sel_CSP_filter * class_1(:,:,i)';
        trans_signal_C2(:,:,i) = sel_CSP_filter * class_2(:,:,i)';

        var_signal1(:,:,i) = var(trans_signal_C1(:,:,i)');
        var_signal2(:,:,i) = var(trans_signal_C2(:,:,i)');
        FEATURE_C1(i, :) = log10(var_signal1(:,:,i)/sum(var_signal1(:,:,i)));
        FEATURE_C2(i, :) = log10(var_signal2(:,:,i)/sum(var_signal2(:,:,i)));
    end
    
    for i = 1: trials
        var_signal11(:,:,i) = var(class_1(:,:,i)');
        var_signal22(:,:,i) = var(class_2(:,:,i)');
        FEATURE_C11(i, :) = log10(var_signal11(:,:,i) / sum(var_signal11(:,:,i)));
        FEATURE_C22(i, :) = log10(var_signal22(:,:,i) / sum(var_signal22(:,:,i)));
    end
    
    scatter3(FEATURE_C1(:,1),FEATURE_C1(:,2), FEATURE_C1(:,4)) 
    hold on 
    scatter3(FEATURE_C2(:,1),FEATURE_C2(:,2), FEATURE_C2(:,4), 'r+')
end