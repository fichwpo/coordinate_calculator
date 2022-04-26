export class RequestBody {
  private dimensions:number[] = [];
  private corners: number[][] = [];

  constructor(dimensions:number[], corners:number[][]){
    this.dimensions = dimensions;
    this.corners = corners;
  }

  
}
