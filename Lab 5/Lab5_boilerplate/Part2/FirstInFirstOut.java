package Part2;

public class FirstInFirstOut implements IPageReplacementStrategy {
    @Override
    /**
     * Returns page faults count using FIFO page replacement algorithm
     * 
     * @param numOfFramesInPhysicalMemory: the physical memory capacity expressed in
     *                                     number of frames. Initially, all
     *                                     numOfFramesInPhysicalMemory are free
     * @param pages:                       the pages references that need to be
     *                                     allocated to the available frames
     */
    public int GetPageFaultsCount(int numOfFramesInPhysicalMemory, int[] pages) {
        // TODO implement First In First Out (FIFO) page replacement algorithm
        return 0;
    }
}
