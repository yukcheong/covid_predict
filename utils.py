import pandas as pd



def changepoints(state):
    if state == "Johor":
        return ['2020-04-01', '2020-04-17', '2020-05-03', '2020-05-19', '2020-06-04', '2020-06-20', '2020-07-06', '2020-07-22', '2020-08-07', '2020-08-23', '2020-09-08', '2020-09-24', '2020-10-10', '2020-10-26', '2020-11-11', '2020-11-27', '2020-12-13', '2020-12-29', '2021-01-14', '2021-01-30', '2021-02-15', '2021-03-03', '2021-03-19', '2021-04-04', '2021-04-20', '2020-11-28','2021-2-3','2021-4-1','2021-06-01','2021-07-01']
    if state == "Kedah":
        return ['2020-04-01', '2020-04-17', '2020-05-03', '2020-05-19', '2020-06-04', '2020-06-20', '2020-07-06', '2020-07-22', '2020-08-07', '2020-08-23', '2020-09-08', '2020-09-24', '2020-10-10', '2020-10-26', '2020-11-11', '2020-11-27', '2020-12-13', '2020-12-29', '2021-01-14', '2021-01-30', '2021-02-15', '2021-03-03', '2021-03-19', '2021-04-04', '2021-04-20', '2021-05-28', '2021-06-25']
    if state == "Kelantan":
        return ['2020-04-01', '2020-04-17', '2020-05-03', '2020-05-19', '2020-06-04', '2020-06-20', '2020-07-06', '2020-07-22', '2020-08-07', '2020-08-23', '2020-09-08', '2020-09-24', '2020-10-10', '2020-10-26', '2020-11-11', '2020-11-27', '2020-12-13', '2020-12-29', '2021-01-14', '2021-01-30', '2021-02-15', '2021-03-03', '2021-03-19', '2021-04-04', '2021-04-28', '2021-05-08', '2021-05-28', '2021-06-30']
    if state == "Melaka":
        return ['2020-04-01', '2020-04-17', '2020-05-03', '2020-05-19', '2020-06-04', '2020-06-20', '2020-07-06', '2020-07-22', '2020-08-07', '2020-08-23', '2020-09-08', '2020-09-24', '2020-10-10', '2020-10-26', '2020-11-11', '2020-11-27', '2020-12-13', '2020-12-29', '2021-01-14', '2021-01-30', '2021-02-15', '2021-03-03', '2021-03-19', '2021-04-04', '2021-04-20', '2021-05-27', '2021-06-15']
    if state == "Negeri Sembilan":
        return ['2020-04-01', '2020-04-17', '2020-05-03', '2020-05-19', '2020-06-04', '2020-06-20', '2020-07-06', '2020-07-22', '2020-08-07', '2020-08-23', '2020-09-08', '2020-09-24', '2020-10-10', '2020-10-26', '2020-11-11', '2020-11-27', '2020-12-13', '2020-12-29', '2021-01-14', '2021-01-30', '2021-02-15', '2021-03-03', '2021-03-19', '2021-04-04', '2021-04-20']
    if state == "Pahang":
        return ['2020-04-01', '2020-04-17', '2020-05-03', '2020-05-19', '2020-06-04', '2020-06-20', '2020-07-06', '2020-07-22', '2020-08-07', '2020-08-23', '2020-09-08', '2020-09-24', '2020-10-10', '2020-10-26', '2020-11-11', '2020-11-27', '2020-12-13', '2020-12-29', '2021-01-14', '2021-01-30', '2021-02-15', '2021-03-03', '2021-03-19', '2021-04-04', '2021-04-20', '2021-06-01', '2021-06-15']
    if state == "Perak":
        return ['2020-04-01', '2020-04-17', '2020-05-03', '2020-05-19', '2020-06-04', '2020-06-20', '2020-07-06', '2020-07-22', '2020-08-07', '2020-08-23', '2020-09-08', '2020-09-24', '2020-10-10', '2020-10-26', '2020-11-11', '2020-11-27', '2020-12-13', '2020-12-29', '2021-01-14', '2021-01-30', '2021-02-15', '2021-03-03', '2021-03-19', '2021-04-04', '2021-04-20', '2021-05-28', '2021-06-20']
    if state == "Perlis":
        return ['2020-04-01', '2020-04-17', '2020-05-03', '2020-05-19', '2020-06-04', '2020-06-20', '2020-07-06', '2020-07-22', '2020-08-07', '2020-08-23', '2020-09-08', '2020-09-24', '2020-10-10', '2020-10-26', '2020-11-11', '2020-11-27', '2020-12-13', '2020-12-29', '2021-01-14', '2021-01-30', '2021-02-15', '2021-03-03', '2021-03-19', '2021-04-04', '2021-04-20']
    if state == "Pulau Pinang":
        return ['2020-04-01', '2020-04-17', '2020-05-03', '2020-05-19', '2020-06-04', '2020-06-20', '2020-07-06', '2020-07-22', '2020-08-07', '2020-08-23', '2020-09-08', '2020-09-24', '2020-10-10', '2020-10-26', '2020-11-11', '2020-11-27', '2020-12-13', '2020-12-29', '2021-01-14', '2021-01-30', '2021-02-15', '2021-03-03', '2021-03-19', '2021-04-04', '2021-04-20', '2021-05-25', '2021-06-28']
    if state == "Sabah":
        return ['2020-04-01', '2020-04-17', '2020-05-03', '2020-05-19', '2020-06-04', '2020-06-20', '2020-07-06', '2020-07-22', '2020-08-07', '2020-08-23', '2020-09-08', '2020-09-24', '2020-10-10', '2020-10-26', '2020-11-11', '2020-11-27', '2020-12-13', '2020-12-29', '2021-01-14', '2021-01-30', '2021-02-15', '2021-03-03', '2021-03-19','2021-05-01', '2021-06-10', '2021-06-23']
    if state == "Sarawak":
        return ['2020-04-01', '2020-04-17', '2020-05-03', '2020-05-19', '2020-06-04', '2020-06-20', '2020-07-06', '2020-07-22', '2020-08-07', '2020-08-23', '2020-09-08', '2020-09-24', '2020-10-10', '2020-10-26', '2020-11-11', '2020-11-27', '2020-12-13', '2020-12-29', '2021-01-14', '2021-01-30', '2021-02-15', '2021-03-03', '2021-03-19', '2021-04-04', '2021-04-20']
    if state == "Terengganu":
        return ['2020-04-01', '2020-04-17', '2020-05-03', '2020-05-19', '2020-06-04', '2020-06-20', '2020-07-06', '2020-07-22', '2020-08-07', '2020-08-23', '2020-09-08', '2020-09-24', '2020-10-10', '2020-10-26', '2020-11-11', '2020-11-27', '2020-12-13', '2020-12-29', '2021-01-14', '2021-01-30', '2021-02-15', '2021-03-03', '2021-03-19', '2021-04-04', '2021-04-20', '2021-05-26', '2021-06-30']
    if state == "W.P. Kuala Lumpur":
        return ['2020-04-01', '2020-04-17', '2020-05-03', '2020-05-19', '2020-06-04', '2020-06-20', '2020-07-06', '2020-07-22', '2020-08-07', '2020-08-23', '2020-09-08', '2020-09-24', '2020-10-10', '2020-10-26', '2020-11-11', '2020-11-27', '2020-12-13', '2020-12-29', '2021-01-14', '2021-01-30', '2021-02-15', '2021-03-03', '2021-03-19', '2021-04-04', '2021-04-20']
    if state == "W.P. Labuan":
        return ['2020-04-01', '2020-04-17', '2020-05-03', '2020-05-19', '2020-06-04', '2020-06-20', '2020-07-06', '2020-07-22', '2020-08-07', '2020-08-23', '2020-09-08', '2020-09-24', '2020-10-10', '2020-10-26', '2020-11-11', '2020-11-27', '2020-12-13', '2020-12-29', '2021-01-14', '2021-01-30', '2021-02-15', '2021-03-03', '2021-03-19', '2021-04-04', '2021-04-20', '2021-05-20', '2021-06-07']
    if state == "W.P. Putrajaya":
        return ['2020-04-01', '2020-04-17', '2020-05-03', '2020-05-19', '2020-06-04', '2020-06-20', '2020-07-06', '2020-07-22', '2020-08-07', '2020-08-23', '2020-09-08', '2020-09-24', '2020-10-10', '2020-10-26', '2020-11-11', '2020-11-27', '2020-12-13', '2020-12-29','2021-01-01', '2021-01-16', '2021-01-30', '2021-02-15', '2021-03-03', '2021-03-19', '2021-04-04', '2021-04-20']
        





def mco(type, days, date):
  
  lower_window = 0
  upper_window = 2
    
  MCO_Phase_One = pd.DataFrame({
  'holiday': 'MCO_Phase_One',
  'ds': pd.date_range(start='3/18/2020', end='3/31/2020'),
  'lower_window': lower_window,
  'upper_window': upper_window,
  })

  MCO_Phase_Two = pd.DataFrame({
  'holiday': 'MCO_Phase_Two',
  'ds': pd.date_range(start='4/1/2020', end='4/14/2020'),
  'lower_window': lower_window,
  'upper_window': upper_window,
  })

  MCO_Phase_Three = pd.DataFrame({
  'holiday': 'MCO_Phase_Three',
  'ds': pd.date_range(start='4/15/2020', end='4/28/2020'),
  'lower_window': lower_window,
  'upper_window': upper_window,
  })

  MCO_Phase_Four = pd.DataFrame({
  'holiday': 'MCO_Phase_Four',
  'ds': pd.date_range(start='4/29/2020', end='5/3/2020'),
  'lower_window': lower_window,
  'upper_window': upper_window,
  })

  CMCO_Phase_One = pd.DataFrame({
  'holiday': 'CMCO_Phase_One',
  'ds': pd.date_range(start='5/4/2020', end='5/12/2020'),
  'lower_window': lower_window,
  'upper_window': upper_window,
  })

  CMCO_Phase_Two = pd.DataFrame({
  'holiday': 'CMCO_Phase_Two',
  'ds': pd.date_range(start='5/13/2020', end='6/9/2020'),
  'lower_window': lower_window,
  'upper_window': upper_window,
  })

  RMCO_Phase_One = pd.DataFrame({
  'holiday': 'RMCO_Phase_One',
  'ds': pd.date_range(start='6/10/2020', end='8/31/2020'),
  'lower_window': lower_window,
  'upper_window': upper_window,
  })

  RMCO_Phase_Two = pd.DataFrame({
  'holiday': 'RMCO_Phase_Two',
  'ds': pd.date_range(start='9/1/2020', end='12/31/2020'),
  'lower_window': lower_window,
  'upper_window': upper_window,
  })

  RMCO_Phase_Three = pd.DataFrame({
  'holiday': 'RMCO_Phase_Three',
  'ds': pd.date_range(start='1/1/2021', end='3/31/2021'),
  'lower_window': lower_window,
  'upper_window': upper_window,
  })

  Total_lockdown = pd.DataFrame({
  'holiday': 'Total_lockdown',
  'ds': pd.date_range(start='6/1/2021', end='6/28/2021'),
  'lower_window': lower_window,
  'upper_window': upper_window,
  })

  if type == "MCO_Phase_One":
      MCO_Phase_One = pd.DataFrame({
      'holiday': 'MCO_Phase_One',
      'ds': (pd.concat(((pd.date_range(start='3/18/2020', end='3/31/2020').to_frame()),(pd.date_range(start=date, periods=days).to_frame())))).index,
      'lower_window': lower_window,
      'upper_window': upper_window,
      })
      
  if type == "MCO_Phase_Two":
      MCO_Phase_One = pd.DataFrame({
      'holiday': 'MCO_Phase_Two',
      'ds': (pd.concat(((pd.date_range(start='4/1/2020', end='4/14/2020').to_frame()),(pd.date_range(start=date, periods=days).to_frame())))).index,
      'lower_window': lower_window,
      'upper_window': upper_window,
      })
      
  if type == "MCO_Phase_Three":
      MCO_Phase_One = pd.DataFrame({
      'holiday': 'MCO_Phase_Three',
      'ds': (pd.concat(((pd.date_range(start='4/15/2020', end='4/28/2020').to_frame()),(pd.date_range(start=date, periods=days).to_frame())))).index,
      'lower_window': lower_window,
      'upper_window': upper_window,
      })
      
  if type == "MCO_Phase_Four":
      MCO_Phase_One = pd.DataFrame({
      'holiday': 'MCO_Phase_Four',
      'ds': (pd.concat(((pd.date_range(start='4/29/2020', end='5/3/2020').to_frame()),(pd.date_range(start=date, periods=days).to_frame())))).index,
      'lower_window': lower_window,
      'upper_window': upper_window,
      })
      
  if type == "CMCO_Phase_One":
      MCO_Phase_One = pd.DataFrame({
      'holiday': 'CMCO_Phase_One',
      'ds': (pd.concat(((pd.date_range(start='5/4/2020', end='5/12/2020').to_frame()),(pd.date_range(start=date, periods=days).to_frame())))).index,
      'lower_window': lower_window,
      'upper_window': upper_window,
      })
      
  if type == "CMCO_Phase_Two":
      MCO_Phase_One = pd.DataFrame({
      'holiday': 'CMCO_Phase_Two',
      'ds': (pd.concat(((pd.date_range(start='5/13/2020', end='6/9/2020').to_frame()),(pd.date_range(start=date, periods=days).to_frame())))).index,
      'lower_window': lower_window,
      'upper_window': upper_window,
      })
      
  if type == "RMCO_Phase_One":
      MCO_Phase_One = pd.DataFrame({
      'holiday': 'RMCO_Phase_One',
      'ds': (pd.concat(((pd.date_range(start='6/10/2020', end='8/31/2020').to_frame()),(pd.date_range(start=date, periods=days).to_frame())))).index,
      'lower_window': lower_window,
      'upper_window': upper_window,
      })
      
  if type == "RMCO_Phase_Two":
      MCO_Phase_One = pd.DataFrame({
      'holiday': 'RMCO_Phase_Two',
      'ds': (pd.concat(((pd.date_range(start='9/1/2020', end='12/31/2020').to_frame()),(pd.date_range(start=date, periods=days).to_frame())))).index,
      'lower_window': lower_window,
      'upper_window': upper_window,
      })
      
  if type == "RMCO_Phase_Three":
      MCO_Phase_One = pd.DataFrame({
      'holiday': 'RMCO_Phase_Three',
      'ds': (pd.concat(((pd.date_range(start='1/1/2021', end='3/31/2021').to_frame()),(pd.date_range(start=date, periods=days).to_frame())))).index,
      'lower_window': lower_window,
      'upper_window': upper_window,
      })
      
  if type == "Total_lockdown":
      MCO_Phase_One = pd.DataFrame({
      'holiday': 'Total_lockdown',
      'ds': (pd.concat(((pd.date_range(start='6/1/2021', end='6/28/2021').to_frame()),(pd.date_range(start=date, periods=days).to_frame())))).index,
      'lower_window': lower_window,
      'upper_window': upper_window,
      })
    
  Movement_Control_Order = pd.concat((MCO_Phase_One, MCO_Phase_Two, MCO_Phase_Three, MCO_Phase_Four, CMCO_Phase_One, CMCO_Phase_Two, RMCO_Phase_One, RMCO_Phase_Two, RMCO_Phase_Three, Total_lockdown))
  
  return Movement_Control_Order

  
