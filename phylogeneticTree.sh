usage() {
    printf "Help:\n[-f] file (fasta file only name and extention)\n[-b] iqtree Boostrap\n[-h] Help\n"
}

FILENAME=
BOOSTRAP=~/sysinfo_page.html

if (($# == 0)); then
  usage
  exit 2
fi

while getopts ":f:b:" opt; do
  case $opt in
    f)
      FILENAME=$OPTARG
      ;;
    b)
      BOOSTRAP=$OPTARG
      ;;
    \?)
      usage
      exit 1
      ;;
    :)
      usage
      exit 1
      ;;
  esac
done

# Check if docker is installed

if [[ $(which docker) ]]
then
    echo "Initial docker steps"
else
    echo "You most need Docker"
    exit 0
fi

# Check if volume is created

if [[ -n $(docker volume ls | grep phylogeneticTreeMapData) ]]
then
    echo "Using existing volume"
else
    echo "Create volume"
    docker volume create --driver local \
      --opt type=none \
      --opt device=$(pwd)/data \
      --opt o=bind \
      phylogeneticTreeMapData
    echo "Success create volume"
fi

# Check if image is created

if [[ -n $(docker images -q phylogenetic-tree-map) ]]
then
    echo "Using existing image"
else
    echo "Create image"
    docker build --tag phylogenetic-tree-map .
    echo "Success create image"
fi

docker run -v phylogeneticTreeMapData:/data phylogenetic-tree-map $FILENAME $BOOSTRAP
