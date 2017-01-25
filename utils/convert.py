"""
Receive kubernetes entity of any type, return valid config for local dev

1. Set replica count to 1
2. Remove resources requests and limitations
3. PV replace type to hostPath
4. Set correct imagePullPolicy
"""


def find_key(conf, key: str):
    """
    Find given key in conf

    :param conf: configuration file
    :param key: key to find
    :return: subdict with key needed
    """
    if isinstance(conf, list):
        for el in conf:
            yield from find_key(el, key)
        return

    if isinstance(conf, dict):
        for conf_key, item in conf.items():
            if conf_key == key:
                yield conf
                continue
            yield from find_key(item, key)


def convert(
        prod_config,
        pull_policy=None
):
    """

    :param prod_config: production config
    :param pull_policy: list of containers with imagePullPolicy: Never
    :return: dev config for minikube
    """

    # set replicas count to 1
    for item in find_key(prod_config, 'replicas'):
        item['replicas'] = 1

    # remove all resources limitation
    resources = list(find_key(prod_config, 'resources'))
    for resource in resources:
        del resource['resources']

    # set pull policy never for given containers
    if pull_policy:
        container_objects = find_key(prod_config, 'containers')
        for containers in container_objects:
            for container in containers['containers']:
                if 'name' in container and container['name'] in pull_policy:
                    container['imagePullPolicy'] = 'Never'

    # fix entity specific stuff
    if 'kind' in prod_config and prod_config['kind'] == 'PersistentVolume':
        pass
