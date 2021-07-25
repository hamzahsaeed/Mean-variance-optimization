# Mean-variance-optimization

Code contains module that calculates optimal weights for a given set of: tickers/combination of tickers, market data(daily returns) and target rate of return
Code executes Markowitz's quadratic optimization technique with an equality constraint (i.e Σw=1) such that weights are optimal allocations to generate the given rate of return while minimizing variance. Solution is given via a quadratic programming equation: 
                                                
                                                min 1/2 w'Q'w + w'c
                                                
                                                s.t Aw=b
                                         where w is a vector of weights, Q is the covariance matrix, c is assumed to be equal to 0,/
                                         A is a matrix of annualized returns for each security and b is the target rate of return
