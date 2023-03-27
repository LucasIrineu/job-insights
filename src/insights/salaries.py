from typing import Union, List, Dict
from src.insights.jobs import read


def get_max_salary(path: str) -> int:
    data = read(path)
    highest_salary = 0

    for job in data:
        if (
            job["max_salary"] != ""
            and job["max_salary"] != "invalid"
            and int(job["max_salary"]) > highest_salary
        ):
            highest_salary = int(job["max_salary"])

    return highest_salary


def get_min_salary(path: str) -> int:
    data = read(path)
    lowest_salary = data[3]['min_salary']

    for job in data:
        if (
            job['min_salary'] != ''
            and job['min_salary'] != 'invalid'
            and int(job['min_salary']) < int(lowest_salary)
        ):
            lowest_salary = int(job['min_salary'])

    return lowest_salary


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    """Checks if a given salary is in the salary range of a given job

    Parameters
    ----------
    job : dict
        The job with `min_salary` and `max_salary` keys
    salary : int
        The salary to check if matches with salary range of the job

    Returns
    -------
    bool
        True if the salary is in the salary range of the job, False otherwise

    Raises
    ------
    ValueError
        If `job["min_salary"]` or `job["max_salary"]` doesn't exists
        If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
        If `job["min_salary"]` is greather than `job["max_salary"]`
        If `salary` isn't a valid integer
    """
    raise NotImplementedError


def filter_by_salary_range(
    jobs: List[dict], salary: Union[str, int]
) -> List[Dict]:
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    raise NotImplementedError
