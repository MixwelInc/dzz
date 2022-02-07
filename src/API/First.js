import {domain} from "../constants";
import axios from "axios";

export default class FirstService {
    static async GetFirstList() {
        const response = await axios.get(`${domain}/first`)
        return response.data
    }

    static async create(name, film, max) {
        const response = await axios.post(`${domain}/first`, {
            full_name: name,
            film: film,
            max: max
        })
        return response.data
    }

}
