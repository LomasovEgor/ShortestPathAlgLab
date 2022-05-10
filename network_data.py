class NetworkData:
    def __init__(self):
        self.test_data = {}
        self.generate_nodes()

    def generate_nodes(self):
        for i in range(10):
            i += 1
            self.test_data[f'{i}'] = {'node': i,
                                      'label': f'{i}',
                                      'title': f'{i}',
                                      'color': '#B0E0E6'}
