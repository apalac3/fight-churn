import pandas as pd
import matplotlib.pyplot as plt

def metric_pair_plot(data_set_path='', metric1='',metric2='',save_path='./'):

    churn_data = pd.read_csv(data_set_path)
    churn_data.set_index(['account_id','observation_date'],inplace=True)

    met1_series = churn_data[metric1]
    met2_series = churn_data[metric2]

    corr = met1_series.corr(met2_series)

    plt.scatter(met1_series, met2_series, marker='.')

    plt.xlabel(metric1)
    plt.ylabel(metric2)
    plt.title('Correlation = %.2f' % corr)
    plt.tight_layout()
    save_name = save_path + '/' + metric1 + '_vs_' + metric2 + '.png'
    plt.savefig(save_name )
    print('Saving plot to %s' % save_name)
    plt.close()
