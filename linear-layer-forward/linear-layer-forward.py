def linear_layer_forward(X: list, W: list, b: list) -> list:
    """
    Returns the affine transformation for every input row.
    """
    # Write code here
    n_samples = len(X)
    d_in = len(X[0])
    d_out = len(W[0])

    ret = []
    for i in range(n_samples):
        arr = []
        for j in range(d_out):
            temp = 0
            for k in range(d_in):
                temp += X[i][k] * W[k][j]

            arr.append(temp + b[j])

        ret.append(arr)

    return ret