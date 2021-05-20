import React, { Component } from 'react';
import axios from 'axios';
import { Table, Tag, Space, Button } from 'antd';
import PubSub from 'pubsub-js' 
import * as echarts from 'echarts';


export default class Piechart extends Component {
    constructor(props) {
        super(props);
        this.state = {
            data:[]
        };
    }
        
    componentWillMount(){
        let url = 'http://localhost:8000/resource_usage';
        axios({
            method: 'get',
            url: url,
        }).then(res => {
            this.setState({
                data:res.data['cpu_usage'] //这里setstate只是让render运行了一次，并没有执行componentDidMount中的内容。所以mychart的option没有改变，图也不会显示,可以选择使用componentDidUpdate或者在更新setstate之后，手动更新一次option
            })
            // updateOption
        })
    }

    componentDidUpdate(){
        var myChart = echarts.init(document.getElementById("pie"),'light');
        var option;
        option = {
            title: {
                text: '任务资源占用情况',
                x: 'center'
            },
            tooltip : {
                trigger: 'item',
                //提示框浮层内容格式器，支持字符串模板和回调函数形式。
                formatter: "{a} <br/>{b} : {c} ({d}%)" 
            },
            series : [
                {
                    name:'订单量',
                    type:'pie',
                    data:this.state.data,
                }
            ],
        }
        myChart.setOption(option);
    }

    handleClick(){
        console.log('click')
        let url = 'http://localhost:8000/resource_usage';
        axios({
            method: 'get',
            url: url,
        }).then(res => {
            console.log(res.data['cpu_usage'])
            var myChart = echarts.init(document.getElementById("pie"),'light');
            var option;
            option = {
                title: {
                    text: '任务资源占用情况',
                    x: 'center'
                },
                tooltip : {
                    trigger: 'item',
                    //提示框浮层内容格式器，支持字符串模板和回调函数形式。
                    formatter: "{a} <br/>{b} : {c} ({d}%)" 
                },
                series : [
                    {
                        name:'订单量',
                        type:'pie',
                        data:res.data['cpu_usage'],
                    }
                ],
            }
            myChart.setOption(option);
        })
    }

    render() {
        return (
            <div>
            <Button type="primary" onClick={this.handleClick}>刷新</Button>
            <div id="pie" style={{ width: '100%', height: 500 }}></div></div>
        )
    }
}

