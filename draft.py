import ast
import tensorflow as tf

a=[[1,2,1,4],[11,2,1,4],[21,2,3,4],[31,2,3,4]]

class TestModel:
    def __init__(self,weights):
        self.weights=weights

        output=weights

        a=[]
        q=tf.FIFOQueue(3,'float')
        self.init=q.enqueue_many(([1.,2.,3.]*10,))

        x=q.dequeue()
        self.x=x

        true_output=[]

        # def fun1():
        #
        #     a.append(tf.constant(1))
        #     return tf.constant(1)
        #
        #
        # def fun2():
        #     a.append(tf.constant(222))
        #     return tf.constant(2)
        #
        # for i in range(4):
        #     true_output.append(tf.cond(output[i] <= 2,lambda: fun1(),lambda :fun2()))
        #     # true_output.append(tf.cond(output[3] <= 2,lambda: output[3],lambda: output[0]-10))
        self.output=true_output
        self.aaa=a

q=tf.FIFOQueue(6000000,'float')
init=q.enqueue_many((a,))
weights=q.dequeue()

testm=TestModel(weights)
fetches = {
    "output": testm.output,
    "aaa":testm.aaa,
    "x":testm.x
}

with tf.Session() as sess:
    # # TODO init.run() 这个run不知道哪里运行
    init.run()
    sess.run(testm.init)

    vals = sess.run(fetches)
    print(vals['output'])
    print(vals['aaa'])
    print(vals['x'])

    vals = sess.run(fetches)
    print(vals['output'])
    # print(vals['aaa'])

    vals = sess.run(fetches)
    print(vals['output'])
    # print(vals['aaa'])

