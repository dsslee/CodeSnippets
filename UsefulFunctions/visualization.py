import matplotlib.pyplot as plt
import matplotlib.pylab as pylab
import seaborn as sns
sns.set()

#===== FIGURE STYLE =====
def figstyle(figsize=(15,5), font='sans-serif', context='notebook', style='whitegrid',):
    
    
    params = {'figure.figsize': figsize,
              'font.family': font,
               'legend.loc': 'best',           
               'xtick.labelsize':'small',
               'ytick.labelsize':'large'
              }
    pylab.rcParams.update(params)
            
    return figstyle(figsize=figsize, font=font, context=context, style=style)
    

#     sns.set(context='notebook', style='whitegrid', palette='deep', font='sans-serif', font_scale=2, color_codes=True, rc=None)


#===== HISTOGRAM & DISTPLOT ======
sns.set(context='notebook', style='whitegrid')
def sns_hist(a, 
             hist=True, bins=None, 
             kde=True, 
             rug=False, 
             #histogram attributes
             hist_kws={'histtype':'bar',
                       'orientation': 'vertical',
                       'log': False, 
                       'stacked': False, 
                       'cumulative':False,
                       'color': 'b', 
                       'lw':None, 
                       'label':None},
             #kde attributes
             kde_kws={"color": "b", 
                      'shade':False},
             
             vertical= False, ax=None):
   
    '''    
    #--- Variable explanation ---#
    a = observed data in 1darray or list
    bins = # of bins
    hist = histogram True/False
    kde =  gaussian kernel density estimate T/F
    rug = rugplot on the support axis T/F
    
    hist_kws
     - histtype: [bar, barstacked, step, stepfilled]
     - orientation: [horizontal, vertical]
     - log: log transform T/F
     - stacked: T/F, 
     - cumulative: T/F,
     - color: color 
     - lw: line width 
     - label: },
    
    kde_kws
     - shade True/False
    vertical = vertical oreintation   
    '''
     
    return sns.distplot(a, bins=bins, hist=hist, kde=kde, rug=rug, 
                        hist_kws=hist_kws, kde_kws=kde_kws, vertical=vertical, ax=ax)

#===== COUNT PLOT ======
def sns_countplot(x, data, y=None,
              hue=None, order=None, orient="v",
              palette=sns.color_palette("RdBu_r"), saturation=1, 
              ax=None):
    
    return sns.countplot(x=x, y=y, data=data, 
                         hue=hue, order=order, orient=orient,
                         palette=palette, saturation=saturation,
                         ax=ax)


#===== COUNT PLOT Horizontal======
def sns_countplot_hor(y, data, x=None,
              hue=None, order=None, orient="h",
              palette=sns.color_palette("RdBu_r"), saturation=1, 
              ax=None):
    
    return sns.countplot(x=x, y=y, data=data, 
                         hue=hue, order=order, orient=orient,
                         palette=palette, saturation=saturation,
                         ax=ax)


#===== SCATTER PLOT ======
def sns_scatter(x, y, hue=None, style=None, size=None, data=None, palette=None, hue_order=None, markers=True, ci=95, n_boot=1000, alpha='auto', legend='brief', ax=None,):

    return sns.scatterplot(x=x, y=y, hue=hue, style=style, size=size, data=data, palette=palette, hue_order=hue_order, markers=markers, ci=ci, n_boot=n_boot, alpha=alpha, legend=legend, ax=ax)


#===== Scatter Line Plot =====
def sns_relplot(data, x, y, hue=None, hue_order=None, kind="scatter",
                col=None, col_order=None, row=None, row_order=None,
                #color attributes
                alpha=None, palette=None, 
                #scatter attributes
                size=None, 
                #line attributes
                style=None, markers=False, ci=None,
                legend='brief', ax=None):
    '''
    #--- Description ---#
    creates subplots with row, col
    creates subgroups with hue
    
    #--- variable explanation ---#
    data = dataframe
    x = x variable
    y = y variable
    hue = adding subgroup
    kind = {scatter, line}
    
    alpha = transparency of color
    palette = color palette
    
    size = marker size
    
    makers = T/F
    style = marker style
    ci = [sd,None,]
    '''
    
    return sns.relplot(data=data, x=x, y=y, hue=hue, hue_order=hue_order, kind=kind, 
                       col=col, col_order=col_order, row=row, row_order=row_order,
                       alpha=alpha, palette=palette,
                       size=size, 
                       style=style, markers=markers, ci=ci,
                       legend=legend, ax=ax)


#===== BOXPLOT =====
sns.set(context='notebook', style='whitegrid')

mnc_palette_5 = ["#0F5BA3", "#3787C0", "#6AADD5", "#ABCFE5", "#D6E5F4"]
mnc_palette_3 = ["#0F5BA3", "#6AADD5", "#D6E5F4"]
mnc_palette_2 = ["#B7C6DF", "#6082B9"]

def sns_boxplot(x, y=None, data=None, hue=None, order=None, orient=None,
                color=None, palette=sns.color_palette("RdBu_r"),
                saturation=1, width=0.8, fliersize=5,
                dodge=True, linewidth=1, whis=1.5, ax=None):
    '''
          order: order categorical level
         orient: {v: vertical, h: horizontal}
          color: 
        palette: default sns.color_palette("GnBu_d")
     saturation: saturation of color
          width: box width
          dodge: T/F option
     fliersize: size of the markers for outliers
      linewidth: width of gray line
           whis: T/F option - Proportion of the IQR past the low and high quartiles to extend the plot whiskers. Points outside this range will be identified as outliers.
    '''
#     palette=sns.color_palette("Blues_r"), 
    return sns.boxplot(x, y=y, data=data, hue=hue, order=order, orient=orient,
                color=color, palette=palette, saturation=saturation, width=width,
                dodge=dodge, fliersize=fliersize, linewidth=linewidth, whis=whis, ax=ax)   


# ===== Train and Test Data Comparison
def compare_tr_te(df1,df2, col_num):
    fig, ax = plt.subplots(figsize=(20,15), nrows=3, ncols=3)
    k=1
    for i in range(3):
        for j in range(3):
            if k < col_num+1:
                sns.distplot(df1.iloc[:, k+1].dropna(), ax=ax[i][j], color='green')
                sns.distplot(df2.iloc[:, k+1].dropna(), ax=ax[i][j], color='red')
                k += 1
    fig.legend(labels=['train', 'test'])
pass
