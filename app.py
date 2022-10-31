from pyflink.datastream import StreamExecutionEnvironment
from pyflink.common.typeinfo import Types
from pyflink.common import Row

env = StreamExecutionEnvironment.get_execution_environment()

def main():
  def my_map_func(row):
    items = [Row('1'), Row('2'), Row('3') ]
    return Row(items)

  ds = env.from_collection(
    collection=[(1, 'aaa'), (2, 'bbb')],
    type_info=Types.ROW([Types.INT(), Types.STRING()]))

  ds2 = ds.map(my_map_func, output_type=Types.ROW([
    Types.LIST(
      Types.ROW([
        Types.STRING(),
      ])
    ),
  ]))

  with ds2.execute_and_collect() as results:
    for result in results:
      print(result)


if __name__ == "__main__":
  main()
