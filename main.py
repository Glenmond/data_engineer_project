import datetime

from crontab import CronTab
from DataLoader import DataLoader
from DataExporter import DataExporter

from UsersPreprocessor import UsersPreprocessor
from PerformancePreprocessor import PerformancePreprocessor
from GoalsPreprocessor import GoalsPreprocessor


if __name__ =="__main__":
    
    batch_id = datetime.date.today().strftime("%y%m%d")

    # Scheduler - Run Once
    # cron = CronTab(user=True)
    # job = cron.new(command='python main.py')

    # job.hour.on(1)
    # job.minute.on(0)
    # cron.write()

    # Data Loader
    data_loader = DataLoader(batch_id)
    data_dict = data_loader.data_dict

    # Data Preprocessor
    users_preprocessor = UsersPreprocessor(batch_id, data_dict['users'])
    performance_preprocessor = PerformancePreprocessor(batch_id, data_dict['performance'])
    goals_preprocessor = GoalsPreprocessor(batch_id, data_dict['goals'])


    # Rearrange into Dictionary of dfs
    data_dict = {
        "users": users_preprocessor.data,
        "performance": performance_preprocessor.data,
        "goals": goals_preprocessor.data
    }

    # Data Exporter
    data_exporter = DataExporter(batch_id, data_dict)
    data_exporter.export_to_csv()